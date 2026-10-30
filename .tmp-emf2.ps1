Add-Type -AssemblyName System.Drawing
$root = (Get-Location).Path + '\web\public\glyphs'
$converted = 0
Get-ChildItem $root -Recurse -File -Include *.jpg,*.jpeg,*.png | ForEach-Object {
  $fs = [System.IO.File]::OpenRead($_.FullName); $buf = New-Object byte[] 4; $n = $fs.Read($buf,0,4); $fs.Close()
  if ($n -eq 4 -and (($buf[0] -eq 1 -and $buf[1] -eq 0 -and $buf[2] -eq 0 -and $buf[3] -eq 0) -or ($buf[0] -eq 0x20 -and $buf[1] -eq 0x45 -and $buf[2] -eq 0x4D -and $buf[3] -eq 0x46))) {
    try {
      $img = [System.Drawing.Image]::FromFile($_.FullName)
      $out = [System.IO.Path]::ChangeExtension($_.FullName,'.png')
      $img.Save($out,[System.Drawing.Imaging.ImageFormat]::Png); $img.Dispose()
      Remove-Item $_.FullName -Force
      $converted++
    } catch {}
  }
}
Write-Output ("converted " + $converted)