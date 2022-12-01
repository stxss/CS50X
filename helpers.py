import re
import asyncio

async def trim_voice(message):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    reply_if_fail = ""
#    while True:
#        if pattern.match(check):
#            await message.reply(message.text)
#            break 
#        else:
#            reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
#            await message.reply(reply_if_fail)
#            break
    if pattern.match(check):

        await message.reply(message.text)

#        break 

    else:

        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"

        await message.reply(reply_if_fail)

       

            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...