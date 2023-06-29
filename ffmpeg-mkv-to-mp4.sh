#!/bin/bash

source="$1"
target="$2"

if [ "$source" == "" ]; then
    echo "[-] missing input"
fi

if [ "$target" == "" ]; then
    fallback=$(basename "$source" .mkv).mp4
    echo "[-] missing output, setting default: $fallback"
    target=$fallback
fi

echo "[+] converting: $source"
echo "[+] destination: $target"

ffmpeg -i "$source" -acodec copy -vcodec copy -strict -2 "$target"
