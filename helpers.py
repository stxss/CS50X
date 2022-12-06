import re
import asyncio
import ffmpeg
import os
import datetime
from os import getenv, listdir, remove
from dotenv import load_dotenv

path = getenv("path")
# Choices for joining


async def trim_file(message, filetype, user_id):
    pattern = re.compile(
        "^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$"
    )
    check = message.text
    reply_if_fail = ""
    if pattern.match(check):
        if os.path.exists(f"downloads/{user_id}_out.mp3"):
            os.remove(f"downloads/{user_id}_out.mp3")

        if filetype == "audio" or filetype == "voice":
            probe_res = ffmpeg.probe(f"downloads/{user_id}_audiofile.mp3")
            in_file = f"downloads/{user_id}_audiofile.mp3"

        duration = probe_res.get("format", {}).get("duration", None)

        user_duration = check.split("-")

        # User input start of trim time
        user_start_time = user_duration[0]
        user_start_mins = int(user_start_time.split(":")[0])
        user_start_sec = int(user_start_time.split(":")[1])

        start_trim_time = user_start_mins * 60 + user_start_sec

        # User input end of trim time
        user_end_time = user_duration[1]
        user_end_mins = int(user_end_time.split(":")[0])
        user_end_sec = int(user_end_time.split(":")[1])

        end_trim_time = user_end_mins * 60 + user_end_sec

        # Recreating the audio file
        input_stream = ffmpeg.input(in_file)
        pts = "PTS-STARTPTS"

        # The actual trim
        file_trim = input_stream.filter_(
            "atrim", start=start_trim_time, end=end_trim_time
        ).filter_("asetpts", pts)

        # Outputting the file
        output = ffmpeg.output(
            file_trim, f"downloads/{user_id}_out.mp3", format="mp3"
        )
        output.run()

    else:
        reply_if_fail = "Invalid range\n\nPlease resend the audio (or forward it again to me) and when selecting the trim option, input a valid range of the times of the desired trim in [mm:ss - mm:ss].\n\nFor example: 00:13-01:40"
        await message.reply(reply_if_fail)


async def create(message, filetype, user_id):
    if os.path.exists(f"downloads/{user_id}_video.mp4"):
        os.remove(f"downloads/{user_id}_video.mp4")
    
    if message == "audio" and filetype == "image":

        # Getting the audio and image files

        input_audio = ffmpeg.input(f"downloads/{user_id}_audiofile.mp3")
        input_image = ffmpeg.input(f"downloads/{user_id}_imagefile.jpg")

        # Setting the width and height of the video

        probe = ffmpeg.probe(f"downloads/{user_id}_imagefile.jpg")
        width = int(probe["streams"][0]["coded_width"])
        height = int(probe["streams"][0]["coded_height"])

        # Outputting the final video

        final_video = ffmpeg.concat(input_image, input_audio, v=1, a=1).filter(
            "scale", width, height
        )
        output = ffmpeg.output(final_video, f"downloads/{user_id}_video.mp4")
        output.run()
