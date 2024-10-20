from datetime import datetime, timedelta
import sys

def mmss(dt):
    mins = int(dt / timedelta(minutes=1))
    secs = int(dt / timedelta(seconds=1))
    remain = (secs - (mins * 60))
    return f"{mins}:{remain}.00"

if len(sys.argv) < 4:
    print("Usage: %s <destination-file> <source-time> <end-time>" % sys.argv[0])
    sys.exit(1)

timefrom = sys.argv[2]
timeto = sys.argv[3]

dtfrom = datetime.strptime(timefrom, '%H:%M:%S')
deltabase = dtfrom - datetime.strptime("00:00:00", '%H:%M:%S')
skip = mmss(deltabase)

dtto = datetime.strptime(timeto, '%H:%M:%S')
deltaend = dtto - datetime.strptime("00:00:00", '%H:%M:%S')
until = mmss(deltaend)

target = sys.argv[1]

cmdline = [f"flac --skip {skip} --until {until} -o line-{target} line.flac"]
cmdline.append(f"flac --skip {skip} --until {until} -o live-{target} live.flac")

print(" && ".join(cmdline))

