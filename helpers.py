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
        user_start_mins = int(start_time.split(":")[0])
        user_start_sec = int(start_time.split(":")[1])
        #print(start_time, user_start_mins, user_start_sec)

        end_time = user_duration[1]
        user_end_mins = int(end_time.split(":")[0])
        user_end_sec = int(end_time.split(":")[1])
        #print(end_time, user_end_mins, user_end_sec)

        file_start_time = "00:00"
        file_end_time = str(datetime.timedelta(seconds=float(duration)))[:-7]

        # Splitting in 0 and 1 because the file_start_time that i wrote is in mm:ss
        file_start_time_mins = file_start_time.split(":")[0] 
        file_start_time_sec = file_start_time.split(":")[1]
        
        # splitting with 1 and 2 because the file time output is in h:mm:ss
        file_end_time_mins = file_end_time.split(":")[1] 
        file_end_time_sec = file_end_time.split(":")[2] 
        print(file_end_time_mins, file_end_time_sec)
        await message.reply(str(datetime.timedelta(seconds=float(duration)))[:-7])
    else:
        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
        await message.reply(reply_if_fail)
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...