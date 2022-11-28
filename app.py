from deepgram import Deepgram
import asyncio, json
import requests
import config
import os

from os import getenv, listdir, remove
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, Update)
from pyrogram.handlers import (callback_query_handler)


load_dotenv()

app = Client(
    "ClipCutBot",
    api_id = getenv("APP_API_ID"),
    api_hash = getenv("APP_API_HASH"),
    bot_token = getenv("API_KEY")
)

deepgram = Deepgram(getenv("DEEPGRAM_API_KEY"))

"Command handling"

@app.on_message(filters.command("start"))
async def help_command(client, message):
    print(message.chat.username, message.text)
    await message.reply("Hi, I'll help you trim your videos")
    await message.reply()

@app.on_message(filters.command("help"))
async def help_command(client, message):
    f = open("help.txt", "r")
    h = f.read()
    await message.reply(h)

@app.on_message(filters.command("transcribe"))
async def help_command(client, message):
    await message.reply("transcribe text")

@app.on_message(filters.command("translate"))
async def help_command(client, message):
    await message.reply("translate text")

@app.on_message(filters.command("join"))    
async def help_command(client, message):
    await message.reply("create a video from the audio + image")

@app.on_message(filters.command("trim"))
async def help_command(client, message):
    await message.reply("trim audio")

@app.on_message(filters.command("timestamp"))
async def help_command(client, message):
    await message.reply("recreate the text from the audio/voice file with timestamps")

@app.on_message(filters.command("search"))
async def help_command(client, message):
    await message.reply("search a string of your choice")

@app.on_message(filters.command("share"))
async def help_command(client, message):
    await message.reply("Share command")


"File handling"

@app.on_message(filters.audio | filters.voice)
async def filter_audio(client, message):

    choices = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Transcribe", callback_data="transcribe"),
                InlineKeyboardButton("Trim audio", callback_data="trim")
            ]
        ]
    )

    await message.reply("Please choose what you want to do with the file", reply_markup=choices)  
    
    audiofile = await message.download()
    sound = open(audiofile, "rb")

    if message.audio:
        mimetype = "audio/mpeg"
    elif message.voice:
        mimetype = "audio/ogg"

    source = {
        "buffer": sound,
        "mimetype": mimetype
    }        

    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                "punctuate": True 
            }
        )
    )
    print(json.dumps(response, indent=4))
    reply = response["results"]["channels"][0]["alternatives"][0]["transcript"]

    #await message.reply(reply)

    dir = config.folder_path
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


#@app.on_callback_query()
#async def choices_first(callback: CallbackQuery):
#    if callback.data == "transcribe":
#        await callback.message.reply("transcribe")
#    elif callback.data == "trim":
#        await callback.message.reply("trim")


app.run()