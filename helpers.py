import re

async def trim(message):
    pattern = re.compile("/^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$/")
    check = message.text
    if pattern.match(check):
        await message.reply(message.text)
    else:
        await message.reply("Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40)")
    

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...