import re
import asyncio
import ffmpeg
import config
import os
import datetime

path = config.path

async def trim_voice(message, filetype):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    reply_if_fail = ""
    if pattern.match(check):
        if filetype == "audio":
            probe_res = ffmpeg.probe("downloads\\audiofile.mp3")
            in_file = "downloads\\audiofile.mp3"            
        elif filetype == "voice":        
            probe_res = ffmpeg.probe("downloads\\voicefile.ogg")
            in_file = "downloads\\voicefile.ogg"

        duration = probe_res.get("format", {}).get("duration", None)
        
        user_duration = check.split("-")
        
        # User input start of trim time 
        user_start_time = user_duration[0]
        user_start_mins = int(user_start_time.split(":")[0])
        user_start_sec = int(user_start_time.split(":")[1])
        
        # User input end of trim time
        user_end_time = user_duration[1]
        user_end_mins = int(user_end_time.split(":")[0])
        user_end_sec = int(user_end_time.split(":")[1])
        

        file_start_time = "00:00"
        file_end_time = str(datetime.timedelta(seconds=float(duration)))[:-7]

        # Splitting in 0 and 1 because the file_start_time that i wrote is in mm:ss
        file_start_time_mins = file_start_time.split(":")[0] 
        file_start_time_sec = file_start_time.split(":")[1]
        
        # splitting with 1 and 2 because the file time output is in h:mm:ss
        file_end_time_mins = file_end_time.split(":")[1] 
        file_end_time_sec = file_end_time.split(":")[2] 
        
        input_stream = ffmpeg.input(in_file)
        pts = "PTS-STARTPTS"
        file_trim = (input_stream.filter_("atrim", start=user_start_time, end=user_end_time).filter_("asetpts", pts))
        output = ffmpeg.output(file_trim, format = "mp3")
        



        await message.reply(str(datetime.timedelta(seconds=float(duration)))[:-7])
    else:
        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
        await message.reply(reply_if_fail)
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...