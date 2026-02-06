# YouTube → MP3 (CLI Thing)

Small Python script to download a YouTube video and turn it into an MP3.
That’s it. No GUI. Just paste link, get file.

It keeps asking for links until you quit.

---

## What it does

* Downloads best available audio
* Converts it to MP3
* Names the file using the video title
* Loops forever until you type `q`

---

## Requirements

* Python 3.8+
* `yt-dlp`
* `ffmpeg` (must be in PATH)

Install stuff:

```bash
pip install yt-dlp
```

Make sure ffmpeg works:

```bash
ffmpeg -version
```

If that prints something that's not an error, you're good.

---

## Run

```bash
python youtube_to_mp3.py
```

Paste link.
Wait.
Done.
Repeat.

Type `q` to quit. or ctrl+c

---

## Notes

* Saves files in the same folder as the script.
* Audio is exported as 192kbps MP3 (change inside script if you care).
* Doesn’t download playlists (on purpose).

---

Use responsibly.
