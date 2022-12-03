import os
import config
import datetime
import ffmpeg



#probe_res = ffmpeg.probe("downloads\\voicefile.ogg")
#duration = probe_res.get("format", {}).get("duration", None)

#print(str(datetime.timedelta(seconds=float(duration)))[:-4])


probe = ffmpeg.probe(f"downloads\971531412\imagefile.jpg")
#width = int(probe['coded_width'])
#height = int(probe['coded_height'])

print(probe["streams"][0]["coded_width"])