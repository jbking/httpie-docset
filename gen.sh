#!/bin/bash -xe

mkdir -p HTTPie.docset/Contents/Resources/Documents/

rst2html5.py README.rst > HTTPie.docset/Contents/Resources/Documents/README.html

cat <<EOF > HTTPie.docset/Contents/Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleIdentifier</key>
  <string>HTTPie</string>
  <key>CFBundleName</key>
  <string>HTTPie</string>
  <key>DocSetPlatformFamily</key>
  <string>httpie</string>
  <key>isDashDocset</key>
  <true/>
  <key>isJavaScriptEnabled</key>
  <false/>
</dict>
</plist>
EOF
