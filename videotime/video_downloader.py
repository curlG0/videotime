import youtube_dl


def download_video(url: str):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        out = ydl.download([url])
        print(out)
