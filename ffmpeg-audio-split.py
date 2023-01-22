from datetime import datetime
import sys

if len(sys.argv) < 5:
    print("Usage: %s <source-file> <destination-file> <source-time> <length>" % sys.argv[0])
    sys.exit(1)

timefrom = sys.argv[3]
timeto = sys.argv[4]

dtfrom = datetime.strptime(timefrom, '%H:%M:%S')
dtto = datetime.strptime(timeto, '%H:%M:%S')
delta = dtto - dtfrom

source = sys.argv[1]
target = sys.argv[2]

cmdline = f"ffmpeg -i {source} -t {delta} -ss {timefrom} -vn -acodec copy -map 0:1 {target}"
print(cmdline)

