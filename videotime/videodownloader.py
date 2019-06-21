import youtube_dl
import os

video = 'https://www.youtube.com/watch?v=KQ6zr6kCPj8'
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    out = ydl.download([video])
    print(out)

