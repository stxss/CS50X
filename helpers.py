import re
import asyncio
import ffmpeg
import config
import os
import datetime

path = config.path

async def trim_voice(message):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    reply_if_fail = ""
    if pattern.match(check):        
        probe_res = ffmpeg.probe("downloads\\voicefile.ogg")
        duration = probe_res.get("format", {}).get("duration", None)
        user_duration = check.split("-")
        start_time = user_duration[0]
        end_time = user_duration[1]
        
        print(user_duration)
        await message.reply(str(datetime.timedelta(seconds=float(duration)))[:-4])
    else:
        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
        await message.reply(reply_if_fail)
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...