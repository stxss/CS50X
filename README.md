# CS50X
 
# **Look-a-Location**
Video Demo:

##     Description:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists in a multi-purpose bot that uses a voice recognition API and other useful libraries like FFMPEG.

A practical use would be, for example:

You are texting with someone and they have some news you need to hear and they send you an audiofile or a voice message but you're at a loud place and can't hear anything or the voice message is too long and you have no time to just listen and scroll back if you've missed something. 

So, instead of either ignoring the message or boringly listen to all of it or posponing and forgetting to listen to it later, you can just redirect this message to the ClipCut Bot in telegram (https://t.me/ClipCutBot) and voilà, in barely any time you can transcribe everything the other person said, even with the option to timestamp the conversation. It also differentiates different speakers, so if the audio had 3 or 4 different people speaking, it will differentiate between all of them!

The other part of the functionality is more of something to have fun, as you can also trim certain parts of said audiofile or just create your kind of meme. Just send the image and the audio you want to join and there you have your own little video in a matter of seconds!

That was the gist of the app. Now onto the specifics and technicalities.



Starting with the what was needed for this bot:

    - Deepgram
    - Telegram Bot
    - Framework to work with, which in this case was Pyrogram

One of the main things that at the start made a difference between the approach was the fact that a lot of Telegram Bots run with asynchronous operations.






The `test_project.py` contains tests for each function of the main project file.


With this final project I was able to implement almost everything from the CS50P course.