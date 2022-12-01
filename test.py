import os
import config
import datetime
import ffmpeg


probe_res = ffmpeg.probe("downloads\\voicefile.ogg")
duration = probe_res.get("format", {}).get("duration", None)

print(str(datetime.timedelta(seconds=float(duration)))[:-4])
