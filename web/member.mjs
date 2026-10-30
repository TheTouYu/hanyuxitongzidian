// member.mjs — 「系统汉字」会员/试用/兑换码（零依赖，JSON 单文件存储）
// 数据文件：web/data/shop.json（首次运行自动创建）
// 设计原则：所有计数与权益判定都在服务端；前端只显示，不参与判断。

import { createHmac, randomBytes, randomUUID, scryptSync, timingSafeEqual } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

// ---------- 档位与规则 ----------

export const TRIAL_LIMIT = 10;      // 每个设备免费提问次数
export const DAILY_CAP = 300;       // 会员每日提问上限（防滥用，非商业限制）
export const CODE_TTL_DAYS = 365;   // 兑换码有效期

export const TIERS = {
  y6:    { id: 'y6',    name: '尝鲜会员', price: 50,  months: 6,  label: '6 个月',  gift: false },
  y16:   { id: 'y16',   name: '年度会员', price: 100, months: 16, label: '16 个月', gift: false },
  life:  { id: 'life',  name: '长期会员', price: 500, years: 10,   label: '10 年',   gift: true  },
};

const TIER_CODE = { y6: 'C6', y16: 'C16', life: 'TY' };

// ---------- 小工具 ----------

const now = () => Date.now();
const iso = (t = now()) => new Date(t).toISOString();

function addMonths(from, n) {
  const d = new Date(from);
  const day = d.getUTCDate();
  d.setUTCDate(1);
  d.setUTCMonth(d.getUTCMonth() + n);
  const last = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0)).getUTCDate();
  d.setUTCDate(Math.min(day, last));
  return d.getTime();
}

function addYears(from, n) {
  const d = new Date(from);
  d.setUTCFullYear(d.getUTCFullYear() + n);
  return d.getTime();
}

export function tierExpiry(tierId, from = now()) {
  const t = TIERS[tierId];
  if (!t) return null;
  return t.months ? addMonths(from, t.months) : addYears(from, t.years);
}

// 去掉容易混淆的 0/O/1/I
const ALPHABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
function block(n) {
  let s = '';
  const b = randomBytes(n);
  for (let i = 0; i < n; i += 1) s += ALPHABET[b[i] % ALPHABET.length];
  return s;
}

export function makeCode(tierId) {
  return `${TIER_CODE[tierId] || 'C'}-${block(4)}-${block(4)}`;
}

const PHONE_RE = /^1[3-9]\d{9}$/;

// 金额只存 6 位小数，避免浮点误差滚雪球
function round6(n) {
  return Math.round((Number(n) || 0) * 1e6) / 1e6;
}

export function isPhone(s) {
  return PHONE_RE.test(String(s || '').trim());
}

// ---------- 存储 ----------

const EMPTY = () => ({
  version: 1,
  seq: 0,
  members: {},   // memberId -> member
  codes: {},     // code -> codeRecord
  orders: {},    // orderId -> order
  trials: {},    // deviceId -> { n, first, last, spent }
  usage: {},     // memberId -> { 'YYYY-MM-DD': n }
  spend: {},     // memberId -> { 'YYYY-MM-DD': 元 }
});

export class Shop {
  constructor(dir) {
    this.dir = dir;
    this.file = join(dir, 'shop.json');
    this.secretFile = join(dir, 'secret.key');
    mkdirSync(dir, { recursive: true });
    this.db = existsSync(this.file) ? {...EMPTY(), ...JSON.parse(readFileSync(this.file, 'utf8'))} : EMPTY();
    if (!existsSync(this.secretFile)) writeFileSync(this.secretFile, randomBytes(32).toString('hex'));
    this.secret = readFileSync(this.secretFile, 'utf8').trim();
  }

  _save() {
    const tmp = `${this.file}.tmp`;
    writeFileSync(tmp, JSON.stringify(this.db, null, 1));
    renameSync(tmp, this.file);
    this._backup();
  }

  // 每天留一份快照（当日第一次保存时写，只增不删）——防误删、可回滚
  _backup() {
    const day = new Date().toISOString().slice(0, 10);
    const f = join(this.dir, `shop-${day}.json`);
    if (existsSync(f)) return;
    try {
      copyFileSync(this.file, f);
    } catch {
      /* 备份失败不影响主流程 */
    }
  }

  _next(prefix) {
    this.db.seq += 1;
    return `${prefix}_${this.db.seq.toString(36).padStart(4, '0')}`;
  }

  // ---------- Cookie 签名 ----------

  sign(value) {
    return createHmac('sha256', this.secret).update(value).digest('hex').slice(0, 32);
  }

  cookie(name, value, maxAge) {
    const v = `${value}.${this.sign(`${name}:${value}`)}`;
    return `${name}=${v}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${maxAge}`;
  }

  verifyNamed(name, raw) {
    if (!raw || typeof raw !== 'string') return null;
    const i = raw.lastIndexOf('.');
    if (i < 0) return null;
    const value = raw.slice(0, i);
    const sig = raw.slice(i + 1);
    const want = this.sign(`${name}:${value}`);
    if (sig.length !== want.length) return null;
    return timingSafeEqual(Buffer.from(sig), Buffer.from(want)) ? value : null;
  }

  // ---------- 设备 / 试用 ----------

  deviceId(req, res) {
    const id = this.verifyNamed('sh_dev', readCookie(req, 'sh_dev'));
    if (id) return id;
    const fresh = randomUUID().replace(/-/g, '');
    res.setHeader('Set-Cookie', this.cookie('sh_dev', fresh, 365 * 24 * 3600));
    return fresh;
  }

  trialOf(deviceId) {
    const t = this.db.trials[deviceId] || { n: 0, first: iso(), last: null, spent: 0 };
    return {
      used: t.n,
      left: Math.max(0, TRIAL_LIMIT - t.n),
      limit: TRIAL_LIMIT,
      spent_yuan: round6(t.spent || 0),
    };
  }

  consumeTrial(deviceId, costYuan = 0) {
    const t = this.db.trials[deviceId] || { n: 0, first: iso(), last: null, spent: 0 };
    t.n += 1;
    t.last = iso();
    t.spent = round6((t.spent || 0) + Math.max(0, Number(costYuan) || 0));
    this.db.trials[deviceId] = t;
    this._save();
    return Math.max(0, TRIAL_LIMIT - t.n);
  }

  refundTrial(deviceId) {
    const t = this.db.trials[deviceId];
    if (!t || t.n <= 0) return;
    t.n -= 1;
    this._save();
  }

  // ---------- 会员 ----------

  memberOf(memberId) {
    if (!memberId) return null;
    const m = this.db.members[memberId];
    if (!m) return null;
    return m;
  }

  memberStatus(m) {
    if (!m || m.revoked) return { active: false, reason: 'revoked' };
    if (m.expires_at && Date.parse(m.expires_at) < now()) return { active: false, reason: 'expired' };
    return { active: true, reason: m.tier };
  }

  usageToday(memberId) {
    const d = new Date().toISOString().slice(0, 10);
    return (this.db.usage[memberId] || {})[d] || 0;
  }

  bumpUsage(memberId) {
    const d = new Date().toISOString().slice(0, 10);
    const u = this.db.usage[memberId] || {};
    u[d] = (u[d] || 0) + 1;
    this.db.usage[memberId] = u;
    this._save();
    return u[d];
  }

  // 会员当天已花掉的模型成本（元）
  spendToday(memberId) {
    const d = new Date().toISOString().slice(0, 10);
    return round6((this.db.spend[memberId] || {})[d] || 0);
  }

  addSpend(memberId, costYuan) {
    const d = new Date().toISOString().slice(0, 10);
    const s = this.db.spend[memberId] || {};
    s[d] = round6((s[d] || 0) + Math.max(0, Number(costYuan) || 0));
    this.db.spend[memberId] = s;
    this._save();
    return s[d];
  }

  // ---------- 账号密码登录 ----------

  findMemberByPhone(phone) {
    const p = String(phone || '').trim();
    if (!p) return null;
    const list = Object.values(this.db.members)
      .filter((m) => m.phone === p)
      .sort((a, b) => String(b.created_at || '').localeCompare(String(a.created_at || '')));
    return list.find((m) => m.pass_hash) || list[0] || null;
  }

  _setPassword(m, password) {
    const salt = randomBytes(16).toString('hex');
    m.pass_salt = salt;
    m.pass_hash = scryptSync(String(password), salt, 32).toString('hex');
    m.pass_set_at = iso();
  }

  setPassword(memberId, password) {
    const m = this.db.members[memberId];
    if (!m) throw new Error('没有这个会员');
    if (String(password || '').length < 6) throw new Error('密码至少 6 位');
    this._setPassword(m, password);
    this._save();
    return m;
  }

  login(phone, password) {
    const m = this.findMemberByPhone(phone);
    if (!m || !m.pass_hash) return { ok: false, error: '手机号或密码不对' };
    if (m.revoked) return { ok: false, error: '这个会员已撤销，请联系主人' };
    const h = scryptSync(String(password || ''), m.pass_salt, 32);
    const want = Buffer.from(m.pass_hash, 'hex');
    if (h.length !== want.length || !timingSafeEqual(h, want)) {
      return { ok: false, error: '手机号或密码不对' };
    }
    if (!this.memberStatus(m).active) return { ok: false, error: '会员已到期，请续费后再登录', member: m };
    return { ok: true, member: m };
  }

  // ---------- 兑换码 ----------

  addCodes(tierId, count, note = '', price = null) {
    if (!TIERS[tierId]) throw new Error('未知档位');
    const n = Math.max(1, Math.min(200, Number(count) || 1));
    const unit = price == null ? TIERS[tierId].price : Math.max(0, Number(price) || 0);
    const out = [];
    for (let i = 0; i < n; i += 1) {
      let code = makeCode(tierId);
      while (this.db.codes[code]) code = makeCode(tierId);
      this.db.codes[code] = {
        code, tier: tierId, price: unit, note,
        status: 'unused', created_at: iso(), used_at: null, member_id: null,
        expires_at: new Date(now() + CODE_TTL_DAYS * 86400000).toISOString(),
      };
      out.push(code);
    }
    this._save();
    return out;
  }

  // 换设备补发：给已有会员生成一个只绑定他的码，兑换后恢复原会员，不新建会员、不记收入
  bindCode(memberId, note = '换设备补发') {
    const m = this.db.members[memberId];
    if (!m) throw new Error('没有这个会员');
    if (m.revoked) throw new Error('这个会员已撤销，不能再补发');
    if (!this.memberStatus(m).active) throw new Error('这个会员已过期，请先续费');
    let code = makeCode(m.tier);
    while (this.db.codes[code]) code = makeCode(m.tier);
    this.db.codes[code] = {
      code, tier: m.tier, price: 0, note: note + '（' + m.phone + '）',
      bind_member: m.id,
      status: 'unused', created_at: iso(), used_at: null, member_id: null,
      expires_at: new Date(now() + CODE_TTL_DAYS * 86400000).toISOString(),
    };
    this._save();
    return { code, member_id: m.id, phone: m.phone };
  }

  listCodes(status) {
    return Object.values(this.db.codes)
      .filter((c) => !status || c.status === status)
      .sort((a, b) => b.created_at.localeCompare(a.created_at))
      .slice(0, 500);
  }

  redeem(codeRaw, phone, password) {
    const code = String(codeRaw || '').trim().toUpperCase();
    if (!isPhone(phone)) return { ok: false, error: '请填写正确的手机号' };
    const c = this.db.codes[code];
    if (!c) return { ok: false, error: '兑换码不存在，请核对后重试' };
    if (c.status !== 'unused') return { ok: false, error: '这个兑换码已经被使用过了' };
    if (c.expires_at && Date.parse(c.expires_at) < now()) return { ok: false, error: '兑换码已过期，请联系我们更换' };
    const pass = String(password || '');
    if (pass && pass.length < 6) return { ok: false, error: '密码至少 6 位' };
    const same = this.findMemberByPhone(phone);
    if (same && same.pass_hash) return { ok: false, error: '这个手机号已经注册过了，请直接用手机号 + 密码登录' };

    // 换设备补发码：只把会员绑到当前浏览器，不新建会员、不记账
    if (c.bind_member) {
      const m = this.db.members[c.bind_member];
      if (!m || m.revoked) return { ok: false, error: '这个会员已失效，请联系我们' };
      if (!this.memberStatus(m).active) return { ok: false, error: '会员已过期，请先续费' };
      c.status = 'used';
      c.used_at = iso();
      c.member_id = m.id;
      if (pass) this._setPassword(m, pass);
      this._save();
      return { ok: true, member: m, rebound: true };
    }

    const started = now();
    const member = {
      id: this._next('m'),
      phone: String(phone).trim(),
      tier: c.tier,
      tier_name: TIERS[c.tier].name,
      started_at: iso(started),
      expires_at: c.tier === 'life' ? iso(tierExpiry('life', started)) : iso(tierExpiry(c.tier, started)),
      code: code,
      gift: TIERS[c.tier].gift,
      gift_sent: false,
      revoked: false,
      created_at: iso(),
    };
    this.db.members[member.id] = member;
    if (pass) this._setPassword(member, pass);
    c.status = 'used';
    c.used_at = iso();
    c.member_id = member.id;
    const orderId = this._next('o');
    this.db.orders[orderId] = {
      id: orderId,
      member_id: member.id,
      phone: member.phone,
      tier: c.tier,
      amount: c.price,
      channel: 'redeem',
      status: 'paid',
      created_at: iso(),
    };
    this._save();
    return { ok: true, member };
  }

  // 线下收款登记：直接建会员 + 记一笔订单（用于微信/现金收款后录单）
  recordOrder({ phone, tier, amount, note, code }) {
    if (!isPhone(phone)) throw new Error('手机号格式不对');
    if (!TIERS[tier]) throw new Error('未知档位');
    const started = now();
    const memberId = this._next('m');
    const codeUsed = code || makeCode(tier);
    if (!this.db.codes[codeUsed]) {
      this.db.codes[codeUsed] = {
        code: codeUsed, tier, price: TIERS[tier].price, note: note || '线下登记',
        status: 'used', created_at: iso(), used_at: iso(), member_id: memberId,
        expires_at: new Date(now() + CODE_TTL_DAYS * 86400000).toISOString(),
      };
    }
    this.db.members[memberId] = {
      id: memberId, phone: String(phone).trim(), tier, tier_name: TIERS[tier].name,
      started_at: iso(started),
      expires_at: iso(tierExpiry(tier, started)),
      code: codeUsed, gift: TIERS[tier].gift, gift_sent: false, revoked: false, created_at: iso(),
    };
    const orderId = this._next('o');
    this.db.orders[orderId] = {
      id: orderId, member_id: memberId, phone: String(phone).trim(), tier,
      amount: Number(amount) || TIERS[tier].price, channel: 'manual',
      note: note || '', status: 'paid', created_at: iso(),
    };
    this._save();
    return { member: this.db.members[memberId], order: this.db.orders[orderId], code: codeUsed };
  }

  revokeMember(memberId) {
    const m = this.db.members[memberId];
    if (!m) return false;
    m.revoked = true;
    m.revoked_at = iso();
    this._save();
    return true;
  }

  markGiftSent(memberId) {
    const m = this.db.members[memberId];
    if (!m) return false;
    m.gift_sent = true;
    m.gift_sent_at = iso();
    this._save();
    return true;
  }

  stats() {
    const members = Object.values(this.db.members);
    const active = members.filter((m) => this.memberStatus(m).active);
    const orders = Object.values(this.db.orders).filter((o) => o.status === 'paid');
    const byTier = {};
    for (const m of members) byTier[m.tier] = (byTier[m.tier] || 0) + 1;
    return {
      members: members.length,
      active: active.length,
      by_tier: byTier,
      revenue: orders.reduce((s, o) => s + (o.amount || 0), 0),
      orders: orders.length,
      codes_unused: Object.values(this.db.codes).filter((c) => c.status === 'unused').length,
      trials: Object.keys(this.db.trials).length,
    };
  }
}

export function readCookie(req, name) {
  const raw = req.headers.cookie || '';
  for (const part of raw.split(';')) {
    const [k, ...rest] = part.trim().split('=');
    if (k === name) return rest.join('=') || null;
  }
  return null;
}
