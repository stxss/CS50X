from deepgram import Deepgram
import asyncio, json
import requests
#from asyncio import run

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

deepgram = Deepgram(getenv("DEEPGRAM_API_KEY"))

"Command handling"

@app.on_message(filters.command("start"))
async def help_command(client, message):
    print(message.chat.username, message.text)
    await message.reply("Hi, I'll help you trim your videos")

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
    print(message.voice, message.audio)

    if message.audio:
        
        #file_url = f'https://api.telegram.org/file/bot{getenv("API_KEY")}/getFile'
        #file_content = f'https://api.telegram.org/file/bot{getenv("API_KEY")}/' + '{file_path}'

#        response = requests.post(url= file_url, params={"file_id": message.audio.file_id})
#        json_response = json.loads(response.content)
#
#        if response.status_code != 200 or not json_response.get("ok"):
#            raise FileNotFoundError()
#        response = requests.post(url= file_content.format(file_path=json_response["result"]["file_path"]))
#        if response.status_code != 200:
#            raise FileNotFoundError()
#        print("all good?")
        
        audiofile = message.download(progress(current, total))
        sound = open(audiofile, "rb")
        mimetype = "audio/mpeg"
        
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
        
        #print(json.dumps(response, indent=4))
        #print(response["results"]["channels"][0]["alternatives"][0]["transcript"])
        
        await message.reply("So that's an audio")
    #elif  message.voice:
    #    
    #    
    #    
    #    await message.reply("So that's a voice message")





    #await message.reply("So that's an audio")


app.run()