#!/bin/bash

SRC="diffCheck.py"
DST="/usr/local/bin/diffCheck"

# Check if source file exists
if [ ! -f "$SRC" ]; then
  echo "❌ File '$SRC' not found in $(pwd)"
  exit 1
fi

# Add executable permission
chmod +x "$SRC"

# Copy to /usr/local/bin
sudo cp "$SRC" "$DST"

# Optional: ensure correct shebang in first line
if ! head -n 1 "$DST" | grep -q '^#!/usr/bin/env python3'; then
  echo "⚠️  Shebang missing. Add '#!/usr/bin/env python3' at the top of $SRC"
fi

echo "✅ diffCheck installed to /usr/local/bin"
echo "➡️  Usage: diffCheck old.txt new.txt"
