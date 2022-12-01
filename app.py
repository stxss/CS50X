from deepgram import Deepgram

import asyncio, json
import requests
import config
import os
import sys
import ffmpeg
import datetime
import helpers
import pyromod.listen
import chat_id
import re

from os import getenv, listdir, remove
from dotenv import load_dotenv
from pyrogram import Client, filters, methods
#from pyrogram.types import (
#    InlineKeyboardButton,
#    InlineKeyboardMarkup,
#    Message,
#    CallbackQuery,
#    Update, 
#    Chat,
#)

from pyrogram.types import *

from pyrogram.handlers import callback_query_handler
from pyrogram.raw import *


load_dotenv()

app = Client(
    "ClipCutBot",
    api_id=getenv("APP_API_ID"),
    api_hash=getenv("APP_API_HASH"),
    bot_token=getenv("API_KEY"),
)

path = config.path

deepgram = Deepgram(getenv("DEEPGRAM_API_KEY"))

"Command handling"


@app.on_message(filters.command("start"))
async def help_command(client, message):
    # print(message.chat.username, message.text)
    await message.reply("Hi, I'll help you trim your videos")


@app.on_message(filters.command("help"))
async def help_command(client, message):
    f = open("help.txt", "r")
    h = f.read()
    await message.reply(h)


@app.on_message(filters.command("transcribe"))
async def transcribe(client, message):
    await message.reply("Please, send an audio file or a voice message!")


@app.on_message(filters.command("translate"))
async def translate(client, message):
    await message.reply("Please, a text to translate")


@app.on_message(filters.command("trim"))
async def trim(client, message):
    await message.reply("trim audio")


@app.on_message(filters.command("join"))
async def join(client, message):
    await message.reply("Please, send an image and a voice file ")


@app.on_message(filters.command("timestamp"))
async def timestamp(client, message):
    await message.reply("recreate the text from the audio/voice file with timestamps")


@app.on_message(filters.command("search"))
async def search(client, message):
    await message.reply("search a string of your choice")


@app.on_message(filters.command("share"))
async def share(client, message):
    await message.reply("Share command")


"File handling"

# Transcription for audio and voice messages with inline keyboard prompt for next actions to take

@app.on_message(filters.audio | filters.voice)
async def filter_audio(client, message):
    print(message)
    chat_id = message.chat.id
    #user_id = message.from_user.id
    #username = message.chat.username

    with open("chat_id.py", "w", encoding="utf-8") as w:
        w.write("chat_id = " + str(chat_id))


    if message.audio:
        audiofile = await message.download(f"audiofile.mp3")
        mimetype = "audio/mpeg"
    elif message.voice:
        audiofile = await message.download(f"voicefile.ogg")
        mimetype = "audio/ogg"

    sound = open(audiofile, "rb")
    source = {"buffer": sound, "mimetype": mimetype}

    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                "punctuate": True,
                "utterances": False,
                "utt_split": 0.8,
                "paragraphs": True,
                "diarize": True,
                "detect_language": True,
            },
        )
    )

    #print(json.dumps(response, indent=4))
    try:
        reply = response["results"]["channels"][0]["alternatives"][0]["paragraphs"][
            "transcript"
        ]
    except KeyError:
        pass

    reply_w_timestamp = ""

    try:
        list_range = len(
            response["results"]["channels"][0]["alternatives"][0]["paragraphs"][
                "paragraphs"
            ]
        )
    except KeyError:
        await message.reply("Something went wrong or your audio was invalid/corrupt.\nPlease try again")

    for i in range(0, list_range + 1):
        for j in range(0, list_range + 2):
            try:
                start_time = response["results"]["channels"][0]["alternatives"][0][
                    "paragraphs"
                ]["paragraphs"][i]["sentences"][j]["start"]
                start = str(datetime.timedelta(seconds=round(start_time, 3)))[:-3]

                end_time = response["results"]["channels"][0]["alternatives"][0][
                    "paragraphs"
                ]["paragraphs"][i]["sentences"][j]["end"]
                end = str(datetime.timedelta(seconds=round(end_time, 3)))[:-3]

                text = response["results"]["channels"][0]["alternatives"][0][
                    "paragraphs"
                ]["paragraphs"][i]["sentences"][j]["text"]

                reply_w_timestamp += start + " to " + end + "\n" + text + "\n\n"
            except:
                continue

    with open(os.path.join(config.path, "transcription.txt"), "w", encoding="utf-8") as w:
        w.write(reply)

    with open(os.path.join(config.path, "transcription_w_timestamp.txt"), "w", encoding="utf-8") as wt:
        wt.write(reply_w_timestamp)

    if message.audio:
        choices = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Transcribe", callback_data="transcribe"),
                    InlineKeyboardButton("Trim audio", callback_data="trim_audio"),
                ],
                [
                    InlineKeyboardButton(
                        "Transcribe w/ timestamps", callback_data="timestamp"
                    )
                ],
            ]
        )
    elif message.voice:
        choices = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Transcribe", callback_data="transcribe"),
                    InlineKeyboardButton("Trim audio", callback_data="trim_voice"),
                ],
                [
                    InlineKeyboardButton(
                        "Transcribe w/ timestamps", callback_data="timestamp"
                    )
                ],
            ]
        )
    await message.reply_text(
        "Please choose what you want to do with the file",
        quote=True,
        reply_markup=choices,
    )


@app.on_message(~filters.audio | ~filters.voice)
async def invalid_file(client, message):
    await message.reply("Invalid file!! Please retry")



# Callback from inline keyboards handling

@app.on_callback_query()
async def choice_from_inline(message, callback: CallbackQuery):
    if callback.data == "trim_audio":
        try:
            trim_length = await app.ask(text="Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40",chat_id=chat_id.chat_id, timeout=30)
            await helpers.trim_voice(trim_length, "audio")

        except asyncio.exceptions.TimeoutError:
            await callback.message.reply("Something went wrong, please try again")
      
    elif callback.data == "trim_voice":
        try:
            trim_length = await app.ask(text="Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40",chat_id=chat_id.chat_id, timeout=30)
            await helpers.trim_voice(trim_length, "voice")

        except asyncio.exceptions.TimeoutError:
            await callback.message.reply("Something went wrong, please try again")
    
        await app.send_audio(chat_id=chat_id, audio="downloads\out.mp3")

    elif callback.data == "transcribe":
        with open(os.path.join(config.path, "transcription.txt"), "r", encoding="utf-8") as f1:
            reply = f1.read()
        await callback.message.reply(reply)
        os.remove("downloads\\transcription.txt")

    elif callback.data == "timestamp":
        with open(
            os.path.join(config.path, "transcription_w_timestamp.txt"), "r", encoding="utf-8"
        ) as f2:
            reply = f2.read()
        await callback.message.reply(reply)
        os.remove("downloads\\transcription_w_timestamp.txt")

        # dir = config.folder_path
        # for f in os.listdir(dir):
        #    os.remove(os.path.join(dir, f))


app.run()
