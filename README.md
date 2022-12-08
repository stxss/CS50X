# CS50X
# **ClipCut, a Telegram Bot**
Video Demo:

#     Description:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists in a multi-purpose bot that uses a voice recognition API and other useful libraries like FFMPEG.

A practical use would be, for example:

You are texting with someone and they have some news you need to hear and they send you an audiofile or a voice message but you're at a loud place and can't hear anything or the voice message is too long and you have no time to just listen and scroll back if you've missed something. 

So, instead of either ignoring the message or boringly listen to all of it or posponing and forgetting to listen to it later, you can just redirect this message to the ClipCut Bot in telegram (https://t.me/ClipCutBot) and voilà, in barely any time you can transcribe everything the other person said, even with the option to timestamp the conversation. It also differentiates different speakers, so if the audio had 3 or 4 different people speaking, it will differentiate between all of them!

The other part of the functionality is more of something to have fun, as you can also trim certain parts of said audiofile or just create your kind of meme. Just send the image and the audio you want to join and there you have your own little video in a matter of seconds!

That was the gist of the app. Now onto the specifics and technicalities.

Starting with the what was needed for this bot:

    - Telegram Bot
    - Deepgram
    - Framework to work with the telegram API, which in this case was Pyrogram (or if you want you can use the raw Telegram API).


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


To start writing this bot without exposing keys and sensitive information, I created a .env file that stored all this information and then loading that info into the main program and 




Using decorators for message handling, where 

```
@app.on_message(filters.command("<command of choice>"))
```