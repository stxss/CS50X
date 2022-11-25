from asyncio import run

from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(
    "ClipCutBot",
    api_id = getenv("APP_API_ID"),
    api_hash = getenv("APP_API_HASH"),
    bot_token = getenv("API_KEY")
)

"Command handling"

@app.on_message(filters.command("start"))
async def help_command(client, message):
    #print(message.chat.username, message.text)
    await message.reply("Hi, I'll help you trim your videos")

@app.on_message(filters.command("help"))
async def help_command(client, message):
    f = open("help.txt", "r")
    h = f.read()
    await message.reply(h)

@app.on_message(filters.command("tv"))
async def help_command(client, message):
    await message.reply("trim the video")

@app.on_message(filters.command("tvo"))
async def help_command(client, message):
    await message.reply("trim the video only (no sound)")

@app.on_message(filters.command("ta"))    
async def help_command(client, message):
    await message.reply("trim the audio only (no video)")

@app.on_message(filters.command("iv"))
async def help_command(client, message):
    await message.reply("isolate the video")

@app.on_message(filters.command("ia"))
async def help_command(client, message):
    await message.reply("isolate audio")

@app.on_message(filters.command("sp"))
async def help_command(client, message):
    await message.reply("separate video and audio files")

@app.on_message(filters.command("share"))
async def help_command(client, message):
    await message.reply("Share command")


"File handling"

@app.on_message(filters.audio)
async def filter_audio(client, message):
    await message.reply("So that's an audio")


app.run()