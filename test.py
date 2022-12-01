import os
import config

#from __future__ import unicode_literals
#import youtube_dl
#
#import json
#import requests
#import urllib.request
#
#
#
##f = open("help.txt", "r")
##print(f.read())
#
#
#url_yt = "https://www.youtube.com/watch?v=3oFAJtFE8YU"
#
#def get_url(url):
#    response = requests.get(url)
#    content = response.content.decode("utf8")
#    return content
#
#def get_json_from_url(url):
#    content = get_url(url)
#    js = json.loads(content)
#    return js
#
#
#class MyLogger(object):
#    def debug(self, msg):
#        pass
#
#    def warning(self, msg):
#        pass
#
#    def error(self, msg):
#        print(msg)
#
#
#def my_hook(d):
#    if d['status'] == 'finished':
#        print('Done downloading, now converting ...')
#
#
##ydl_opts = {
##    'format': 'bestaudio/best',
##    'postprocessors': [{
##        'key': 'FFmpegExtractAudio',
##        'preferredcodec': 'mp4',
##        'preferredquality': '192',
##    }],
##    'logger': MyLogger(),
##    'progress_hooks': [my_hook],
##}
#ydl_opts= {}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=3oFAJtFE8YU'])
import os
#import ffmpeg
from ffmpeg import _probe

probe_res = ffmpeg._probe("voicefile.ogg")
duration = probe_res.get("format", {}).get("duration", None)

print("hello")



