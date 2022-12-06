from deepgram import Deepgram  # API for voice recognition

import asyncio
#import config
import os
import datetime
import time
import helpers
import pyromod.listen
import shutil, stat
import schedule
from threading import Timer

from os import getenv, listdir, remove
from dotenv import load_dotenv
from pyrogram import (
    Client,
    filters,
    methods,
)  # Library that will be used for this telegram bot

from pyrogram.types import *
from pyrogram.raw import *


# Loading necessary keys and api data
load_dotenv()

app = Client(
    "ClipCutBot",
    api_id=getenv("APP_API_ID"),
    api_hash=getenv("APP_API_HASH"),
    bot_token=getenv("API_KEY"),
)

#path = config.path
path = getenv("PATH")

deepgram = Deepgram(getenv("DEEPGRAM_API_KEY"))


# Command handling

@app.on_message(filters.command("path"))
async def help_command(client, message):
    await message.reply(f"{os.path.dirname(__file__)}")

@app.on_message(filters.command("start"))
async def help_command(client, message):
    await message.reply("Hi, I'll help you transcribe or trim your audiofile and more!")


@app.on_message(filters.command("help"))
async def help_command(client, message):
    f = open("help.txt", "r")
    h = f.read()
    await message.reply(h)


@app.on_message(filters.command("transcribe"))
async def transcribe(client, message):
    await message.reply(
        "Please, send an audio file or a voice message and click 'Transcribe' or 'Transcribe w/timestamps'!"
    )


@app.on_message(filters.command("trim"))
async def trim(client, message):
    await message.reply(
        "Please, send an audio file or a voice message and click 'Trim audio'!"
    )


@app.on_message(filters.command("join"))
async def join(client, message):
    await message.reply("Please, send an image and an audiofile and then click 'Join'")


"File handling"

# Transcription for audio and voice messages with inline keyboard prompt for next actions to take


@app.on_message(filters.audio | filters.voice)
async def filter_audio(client, message):
    print(message)
    chat_id = message.chat.id

    # If a message is an audio or voice file, it downloads the files into the respective folder
    if message.audio or message.voice:
#        audiofile = await message.download(f"downloads\\{chat_id}\\audiofile.mp3")
        audiofile = await message.download()


        mimetype = "audio/mpeg"

    # A flag for the existence of an image is set. If there is already an image sent from a certain user, the flag is set to True, if not, it is set to False
    # This helps when calling the join function, as if there wasn't an image I couldn't solve a input verification like one does with synchronous functions (aka try except block)
    # So I opted for a state dictionary in the form of a .py file that contains a chat_id and the boolean value of a sent_img flag.

    if os.path.exists(os.path.join(path, f"{chat_id}\\imagefile.jpg")):
        with open(f"downloads\{chat_id}\chat_id.py", "w", encoding="utf-8") as w:
            w.write(f"chat_id = {chat_id}\n")
            w.write("sent_img = True")
    else:
        with open(f"downloads\{chat_id}\chat_id.py", "w", encoding="utf-8") as w:
            w.write(f"chat_id = {chat_id}\n")
            w.write("sent_img = False")

    # Making use of the Deepgram API, where a mimetype and an audiofile are set

    sound = open(audiofile, "rb")
    source = {"buffer": sound, "mimetype": mimetype}

    # Punctuate is for punctuation of the recognized voice
    # Utterances is for the separation of phrases, into meaningful semantic units
    # utt_split is the time sensibility of said utterances
    # Paragraphs is similar to utterances but it is to separate in a more appealing appearance
    # Diarize is for the differentiation of speakers, i.e if there are different voices in an audiofile, there is a separation between speaker 0, speaker 1, etc.
    # Detect_language is for the detection of all languages supported by Deepgram, which can be verified here: https://developers.deepgram.com/documentation/features/language/

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

    # This try except block just fetches the transcription from the audiofile
    try:
        reply = response["results"]["channels"][0]["alternatives"][0]["paragraphs"][
            "transcript"
        ]
    except KeyError:
        pass

    reply_w_timestamp = ""

    # Same as above, but for paragraphs
    try:
        list_range = len(
            response["results"]["channels"][0]["alternatives"][0]["paragraphs"][
                "paragraphs"
            ]
        )
    except KeyError:
        await message.reply(
            "Something went wrong or your audio was invalid/corrupt.\nPlease try again"
        )

    # Printing the transcriptions with timestamps
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

    # Saving the transcriptions to separate files
    #with open(
    #    os.path.join(getenv("path"), f"{chat_id}\\transcription.txt"),
    #    "w",
    #    encoding="utf-8",
    #) as w:
    #    w.write(reply)

    with open(os.path.join(os.path.dirname(__file__), f"downloads\\{chat_id}\\transcription.txt"), "w", encoding="utf-8") as w:
        w.write(reply)
    
    with open(
        os.path.join(os.path.dirname(__file__), f"downloads\\{chat_id}\\transcription_w_timestamp.txt"),
        "w",
        encoding="utf-8",
    ) as wt:
        wt.write(reply_w_timestamp)

    # Prompting the user with a choice for what to do with the audiofile, where transcribe is to receive the transcriptions, timestamp for the transcription with timestamps
    # trim_audio for a option of trimming the audio
    # join for creating a video from an image and an audio of choice

    if message.audio or message.voice:
        choices = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Transcribe", callback_data="transcribe"),
                    InlineKeyboardButton(
                        "Transcribe w/ timestamps",
                        callback_data="timestamp",
                    ),
                ],
                [
                    InlineKeyboardButton("Trim audio", callback_data="trim_audio"),
                    InlineKeyboardButton("Join", callback_data="join"),
                ],
            ]
        )

    await message.reply_text(
        "Please choose what you want to do with the file",
        quote=True,
        reply_markup=choices,
    )


# Handling of any type of file that isn't an audiofile, a voice message or a photo
@app.on_message(~filters.audio | ~filters.voice | filters.media)
async def invalid_file(client, message):

    if str(message.media) == "MessageMediaType.PHOTO":
        maintain_chat_id = str(message.chat.id)
        imagefile = await message.download(
            f"downloads\\{maintain_chat_id}\\imagefile.jpg"
        )
        with open("chat_id.py", "w", encoding="utf-8") as w:
            w.write(f"chat_id = {maintain_chat_id}\n")
            w.write("sent_img = True")

        await message.reply("Please, send an audio file and click 'Join'")
    else:
        await message.reply(
            "Please, send a valid message. It should be either a voice or audio file."
        )


# Callback from inline keyboards handling


@app.on_callback_query()
async def choice_from_inline(Client, callback: CallbackQuery):

    # Reading from the state dictionary, the chat_id, which is unique to every user and state of sent_image

    with open(
        f"downloads\\{callback.from_user.id}\chat_id.py", "r", encoding="utf-8"
    ) as f:
        for line in f:
            if line.startswith("chat_id"):
                chat_id_for_join = line[9:]
            if line.startswith("sent_img"):
                sent_img_val = line[10:]

    # Handling of the trim option
    if callback.data == "trim_audio":
        try:
            trim_length = await app.ask(
                text="Please send the times of the desired trim in [mm:ss - mm:ss].\nFor example: 00:13-01:40",
                chat_id=chat_id_for_join.strip(),
                timeout=30,
            )

            # Calling a helper function for trimming the audio
            await helpers.trim_file(trim_length, "audio", chat_id_for_join.strip())

            # Sending the trimmed audio back to the user
            await app.send_audio(
                chat_id=chat_id_for_join.strip(),
                audio=os.path.join(os.path.dirname(__file__), f"downloads\\{chat_id_for_join.strip()}\\out.mp3"),
            )

            # Removing the file from the folder, because it is of no longer use and so it can no longer be accessed
            os.remove(f"downloads\{chat_id_for_join.strip()}\\out.mp3")

        except asyncio.exceptions.TimeoutError:
            await callback.message.reply("Something went wrong, please try again")

    # Handling the click of the transcription and transcription w/timestamps buttons
    elif callback.data == "transcribe":
        with open(os.path.join(os.path.dirname(__file__), f"downloads\\{chat_id_for_join.strip()}\\transcription.txt"),
            "r",
            encoding="utf-8",
        ) as f1:
            reply = f1.read()
        await callback.message.reply(reply)

        # Deleting the file after it is sent to the user and so it can no longer be accessed
        os.remove(f"downloads\{chat_id_for_join.strip()}\\transcription.txt")

    elif callback.data == "timestamp":
        with open(
            os.path.join(os.path.dirname(__file__),
                f"downloads\\{chat_id_for_join.strip()}\\transcription_w_timestamp.txt",
            ),
            "r",
            encoding="utf-8",
        ) as f2:
            reply = f2.read()
        await callback.message.reply(reply)

        # Deleting the file after it is sent to the user and so it can no longer be accessed
        os.remove(
            f"downloads\{chat_id_for_join.strip()}\\transcription_w_timestamp.txt"
        )

    # Handling the join button
    elif callback.data == "join":

        if not sent_img_val.strip() == "True":
            await app.send_message(
                chat_id=chat_id_for_join.strip(), text="Please send an image"
            )
        else:
            try:

                # Calling a helper function to create a video
                await helpers.create("audio", "image", chat_id_for_join.strip())

                # Sending the video back to the user
                await app.send_video(
                    chat_id=chat_id_for_join.strip(),
                    video=os.path.join(os.path.dirname(__file__), f"downloads\\{chat_id_for_join.strip()}\\video.mp4"
                    ),
                )

                # Deleting the file as it is no longer needed and can no longer be accessed
                os.remove(f"downloads\{chat_id_for_join.strip()}\\video.mp4")
            except:
                await callback.message.reply("Something went wrong, please try again")


if __name__ == "__main__":

    # Running the app
    app.run()

    # If the app is closed/terminated, delete the downloads folder, which contains the chat_id's of the users
#    dir = getenv("PATH")
#
#    def remove_readonly(func, dir, _):
#        os.chmod(dir, stat.S_IWRITE)
#        func(dir)
#
#    shutil.rmtree(dir, onerror=remove_readonly)
