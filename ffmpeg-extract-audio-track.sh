#!/bin/bash

source="$1"
track="$2"
target="$3"

if [ "$source" == "" ]; then
    echo "[-] missing input"
    exit 1
fi

if [ "$target" == "" ]; then
    fallback=$(basename "$source" .mkv)-track-${track}.flac
    echo "[-] missing output, setting default: $fallback"
    target=$fallback
fi

echo "[+] converting: $source"
echo "[+] destination: $target"

ffmpeg -i "$source" -vn -map 0:$track -acodec copy "$target"

