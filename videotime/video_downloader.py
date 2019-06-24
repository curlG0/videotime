import youtube_dl


def download_video(url: str, output: str):
    ydl_opts = {
        'outtmpl': output
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def get_info(url: str):
    with youtube_dl.YoutubeDL({}) as ydl:
        return ydl.extract_info(url, download=False, force_generic_extractor=False)
