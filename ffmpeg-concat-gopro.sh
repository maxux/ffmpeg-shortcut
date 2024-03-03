#!/bin/bash
ffmpeg -f concat -safe 0 -i <(for f in ./*.MP4; do echo "file '$PWD/$f'"; done) -c copy merge.mp4
