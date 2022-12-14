# CS50X
# **ClipCut, a Telegram Bot**
Video Demo: https://youtu.be/rjCBLUduMQQ

# **Description**:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists in a multi-purpose bot that uses a voice recognition API and other useful libraries like FFMPEG. 
<br></br>

## **A practical use**

You are texting with someone and they have some news you need to hear and they send you an audiofile or a voice message but you're at a loud place and can't hear anything or the voice message is too long and you have no time to just listen and scroll back if you've missed something. 

So, instead of either ignoring the message or boringly listen to all of it or postponing and forgetting to listen to it later, you can just redirect this message to the ClipCut Bot in telegram (https://t.me/ClipCutBot) and voilà, in barely any time you can transcribe everything the other person said, even with the option to timestamp the conversation. It also differentiates different speakers, so if the audio had 3 or 4 different people speaking, it will differentiate between all of them!

The other part of the functionality is more of something to have fun, as you can also trim certain parts of said audiofile or just create your kind of meme. Just send the image and the audio you want to join and there you have your own little video in a matter of seconds!
<br></br>

## **That was the gist of the app. Now onto the specifics and technicalities.**

Starting with the what was needed for this bot:

    - Telegram Bot
    - Deepgram or a Voice Recognition API of your choice
    - Framework to work with the telegram API, which in this case was Pyrogram (or if you want you can use the raw API).

A quick touch on Deepgram. It is a transcription and speech understanding API. I used this as it was a good and accessible way of transcribing audio files, as I simply didn't have the time nor the resources to train my own Neural Network to recognize human speech.

So, one of the first and main things that at the start made a difference between the approach was the fact that a lot of Telegram Bots run with asynchronous operations. And while they seem strange at first they are pretty quick to get used to.

```
# functions that are defined synchronously can only run one operation at a time 

def func():
    #code
    return result
```

```
# functions that are defined asynchronously can run multiple operations at a time, as they are non-blocking, which means they can send multiple requests to a server

async def func():
    #code
    await result
```

Now, onto the code.

First, I want to be able to handle commands that users send. So, some useful commands for this bot would be:


    - /start - to start the bot
    - /help for information on how to use the bot!
<br>

## **Then, the gist of the app**

    -/transcribe - transcribe the audio or voice file
    -/trim - trim audio file
    -/join - create a video from the audio and an image of your choice


This bot works as follows:

You can send or forward a voice message, audio file or image.
When sending a audio/voice message, you are prompted to choose what you want to do with the file:

- Have it transcribed, optionally, with timestamps that are represented as [h : mm : ss : milliseconds]

- Trim the audio in a [mm : ss] format. If choosing a time that goes beyond the length of the recording, it is capped to the end of the file. 

- Join an audio and an image of your choice. (Shine with your meme making capabilities)

- Extract the audio from a video of your choice

To start writing this bot without exposing keys and sensitive information, I created a `.env` file that stored all this information and then loading that info into the main program and a .gitignore file which allowed for this information protection. Had to learn the hard way to avoid creating a `config.py` instead of a `.env` file to achieve the same thing, as this later caused problems with paths of files when deploying the application. So, for anyone reading this, use `.env`.

Starting up a telegram bot session in a form of a pyrogram Client, I import the voice recognition API key, and the Telegram Bot token which I got from BotFather, a bot that allows me to even create my own application on telegram.

Using decorators for message handling, where 

```
@app.on_message(filters.command("<command of choice>"))
async def <your_command>(client, message):
    await message.reply("your message")
```
triggers a message back from the bot when you type a /command and send to the bot. These were used to just invoke the user to send files and help with guiding the user

## **File Handling**

Upon sending a voice or an audiofile, the same type of decorator as before catches it and because I applied filters to the decorator, such as ```(filters.audio | filters.voice)``` it executes the lines for downloading the file and setting the mimetype variable that is necessary for the transcription API.

For ease of use and to avoid complications, because telegram's voice files usually have the ```.ogg``` extension and audiofiles have an ```.mp3``` extension, I converted every audio to have the ```.mp3``` extension.

Then, I set a file to have a ```chat_id``` of a user and a ```set_img``` boolean value. This is to check if a user has sent any image yet, to be able to use the join function later.

Then, the bot transcribes and creates two files, one for a normal transcription and another for a transcription with timestamps. Each file, upon being sent to the user, is deleted from the system.

<br>

## **But how are the files sent?**

Telegram has inline buttons, which I make use of. When a user sends a valid message (voice, audio or image) this keyboard is prompted, where the user chooses what to do next.

For the transcription options, it's pretty straightforward but for the join and trim options it's a bit trickier.

This is where the helpers come to play. 

Here, I make use of FFMPEG a complete, cross-platform solution to record, convert and stream audio and video. This is a go-to library for media manipulation. Many people even build their own screen/media recording software and programs out of FFMPEG's source code and build.

The trim function begins with checking if the user has written valid trim parameters, which are checked via a regex pattern. If everything is good here, the audio or video file is trimmed and then sent back to the user

In the case of the user sending a video file, I allow for basically the same options, but I also offer the possibility to extract the audio from the video rather than joining it with something else, which wouldn't really make sense.

The create function is responsible for the "join" button, where the user can join a video and an audio of their choice and this is where the flag which I mentioned earlier is checked, if ```sent_img``` is True or False. If this variable is False, it prompts the user to send an image. If it is True, it proceeds to create a video and then sends it back to the user.

<br>
Now, the bot is complete and all that is needed is the option to deploy it. I chose to deploy it and make it useful to the public. But as soon as the credits from the trial on Deepgram and Railway end, the bot unfortunately ends its service as well, or maybe I'll change my mind if it gets used plenty.
<br></br>

I learned a lot in the process of working with this bot, specifically:
    
- Deepened my knowledge of python
- Learned how to work with various API's  
- Learned how to create and manage a project through GitHub Desktop
- Learned Docker
- Learned how to deploy an app

It is worth mentioning, that I am by far a seasoned professional with any of these tools, as a lot of what I've learned was on a rudimentary level but it wes a lot of fun and I'll definetely want to learn and get more knowledgeable in these topics, softwares and systems.

And with this, I got to thank all of CS50's staff for their amazing course, which was an amazing introduction that helped me progress and fundamentally, it taught me to teach myself how to code.
