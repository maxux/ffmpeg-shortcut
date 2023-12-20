from datetime import datetime
import sys

if len(sys.argv) < 4:
    print("Usage: %s <destination-file> <source-time> <end-time>" % sys.argv[0])
    sys.exit(1)

timefrom = sys.argv[2]
timeto = sys.argv[3]

dtfrom = datetime.strptime(timefrom, '%H:%M:%S')
dtto = datetime.strptime(timeto, '%H:%M:%S')
delta = dtto - dtfrom

target = sys.argv[1]

cmdline = [f"ffmpeg -i line.flac -t {delta} -ss {timefrom} -vn -acodec copy line-{target}"]
cmdline.append(f"ffmpeg -i live.flac -t {delta} -ss {timefrom} -vn -acodec copy live-{target}")

print(" && ".join(cmdline))

