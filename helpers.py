import re

async def trim_voice(message):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    reply_if_fail = ""
    while True:
        await message.reply(reply_if_fail)
        if not pattern.match(check):
            reply_if_fail = "Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40"
            #await message.reply("Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40")
            await message.reply(reply_if_fail)
            continue
        else:
            await message.reply(message.text)
            break
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...