import re

async def trim(message):
    pattern = re.compile("^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$")
    check = message.text
    while True:
        if not pattern.match(check):
            await message.reply("Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40")
            continue
        else:
            await message.reply(message.text)
            break
            

    
    
    
    
    






async def join(message):
    ...

async def translate(message):
    ...