#!/usr/bin/env bash
set -euo pipefail

if [[ -f "dist/QuoteBook-mac.dmg" ]]; then
  echo "dist/QuoteBook-mac.dmg already exists."
  exit 0
fi

app_path="$(find dist -maxdepth 3 -type d -name 'QuoteBook.app' | head -n 1)"
if [[ -z "$app_path" ]]; then
  echo "Could not find QuoteBook.app under dist/."
  find dist -maxdepth 3 -print || true
  exit 1
fi

echo "Creating fallback DMG from $app_path"
rm -f dist/QuoteBook-mac.dmg
hdiutil create \
  -volname "QuoteBook" \
  -srcfolder "$app_path" \
  -ov \
  -format UDZO \
  dist/QuoteBook-mac.dmg
