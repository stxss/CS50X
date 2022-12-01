import re
import asyncio
import ffmpeg
import config
import os

path = config.path

async def trim_voice(message):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    reply_if_fail = ""
    if pattern.match(check):
        await message.reply(message.text)
        with open(os.path.join(config.path, "voicefile.ogg"), "w", encoding="utf-8") as v:
            os.system('ffprobe -i v -show_entries format=duration -v quiet -of csv="p=0"')
    else:
        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
        await message.reply(reply_if_fail)
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...