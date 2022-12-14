import re
import asyncio
import ffmpeg
import os
import datetime
from os import getenv, listdir, remove
import sys

from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata, bash
from ethon.pyutils import rename

# Choices for joining


async def trim_file(message, filetype, user_id):
    pattern = re.compile(
        "^(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))-(([0]?[0-5][0-9]|[0-9]):([0-5][0-9]))$"
    )
    check = message.text
    reply_if_fail = ""
    if pattern.match(check):
        if filetype == "audio":
            if os.path.exists(f"downloads/{user_id}_out.mp3"):
                os.remove(f"downloads/{user_id}_out.mp3")
            in_file = f"downloads/{user_id}_audiofile.mp3"
        elif filetype == "video":
            if os.path.exists(f"downloads/{user_id}_trimmed_video.mp4"):
                os.remove(f"downloads/{user_id}_trimmed_video.mp4")
            in_file = f"downloads/{user_id}_video_from_user.mp4"

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
        if filetype == "audio":
            file_trim = input_stream.filter_(
                "atrim", start=start_trim_time, end=end_trim_time
            ).filter_("asetpts", pts)

            # Outputting the file

            output = ffmpeg.output(
                file_trim, f"downloads/{user_id}_out.mp3", format="mp3"
            ).run()

        # The actual trim for the video
        if filetype == "video":
            video_trim = input_stream.trim(
                start=start_trim_time, end=end_trim_time
            ).setpts(pts)

            audio_trim = input_stream.filter_(
                "atrim", start=start_trim_time, end=end_trim_time
            ).filter_("asetpts", pts)

            video_and_audio = ffmpeg.concat(video_trim, audio_trim, v=1, a=1)

            # Outputting the file

            #output = ffmpeg.output(
            #    video_and_audio, f"downloads/{user_id}_trimmed_video.mp4", format="mp4"
            #).run()

            bash(f'ffmpeg -i {in_file} -ss {start_trim_time} -to {end_trim_time} -acodec copy -vcodec copy downloads/{user_id}_trimmed_video.mp4')

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

        # Outputting the final video

        final_video = ffmpeg.concat(input_image, input_audio, v=1, a=1)
        output = ffmpeg.output(final_video, f"downloads/{user_id}_video.mp4")
        output.run()

        # bash(f'ffmpeg -y -i {input_image} -i {input_audio} -c:a copy downloads/{user_id}_video.mp4')


async def extract(message, user_id):
    if os.path.exists(f"downloads/{user_id}_extracted_audio.mp3"):
        os.remove(f"downloads/{user_id}_extracted_audio.mp3")
    in_file = f"downloads/{user_id}_video_from_user.mp4"

    if message == "video_from_user":
        input_stream = ffmpeg.input(in_file)
        pts = "PTS-STARTPTS"

        extracted_audio = input_stream.filter_("atrim").filter_("asetpts", pts)

        # Outputting the file
        output = ffmpeg.output(
            extracted_audio, f"downloads/{user_id}_extracted_audio.mp3", format="mp3"
        ).run()

    # if message == "video_from_user":
    #    bash(f"ffmpeg -i downloads/{user_id}_video_from_user.mp4 -vn -acodec copy downloads/{user_id}_extracted_audio.mp3")


# Okay, for some reason, the ffmpeg commands started working in pythonic style in the docker/deployed server only
# after installing ethon. I do not know the reason behind this and why, but it works and I am glad it does
