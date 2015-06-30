#!/usr/bin/env python

import youtube_dl
import os
import subprocess
import signal
import sys

def sig_handler(signal, frame):
   sys.exit(0)

if "__main__" == __name__:

   signal.signal(signal.SIGINT, sig_handler)
   os.chdir('/home/arun/Music/youtube')
   ydl_opts = {
      'format' : 'bestaudio/best',
      'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '320',
        }],
       }

url = raw_input("Enter URL> ").strip()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   ydl.download([url])
