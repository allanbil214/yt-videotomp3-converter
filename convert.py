import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # filename = video title
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # clean 192kbps mp3
        }],
        'quiet': False,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download complete.\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")


def main():
    print("=== YouTube to MP3 Downloader ===")
    print("Type 'q' to quit.\n")

    while True:
        url = input("Enter YouTube URL: ").strip()

        if url.lower() == 'q':
            print("Goodbye 👋")
            break

        if not url:
            print("Please enter a valid URL.\n")
            continue

        download_audio(url)


if __name__ == "__main__":
    main()
