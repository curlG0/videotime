import youtube_dl


def download_video(url: str, output: str):
    ydl_opts = {
        'outtmpl': output
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        out = ydl.download([url])
        print(out)
