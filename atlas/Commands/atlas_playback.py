import urllib.parse
import webbrowser
import yt_dlp
from atlas.Software.tts import speak

# ---------- YouTube Play (yt_dlp) ----------
def play_on_youtube(song_name):
    query = urllib.parse.quote(song_name)
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch',
        'noplaylist': True,
        'extract_flat': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        if 'entries' in info and len(info['entries']) > 0:
            video_url = info['entries'][0]['url']
            speak(f"Playing {song_name} on YouTube.")
            print(f"Opening: {video_url}")
            webbrowser.open(video_url)
        else:
            speak("I couldn't find that song on YouTube.")


# ---------- Other Players ----------
def other_player(command):
    # Detect platform name from "play ... on <platform>"
    platform_match = command.split("on")[-1].strip()
    song_name = command.replace("play", "").replace(f"on {platform_match}", "").strip()
    query = urllib.parse.quote(song_name)

    if "spotify" in platform_match:
        url = f"https://open.spotify.com/search/{query}"
        speak(f"Searching for {song_name} on Spotify.")
    elif "jiosaavn" in platform_match or "saavn" in platform_match:
        url = f"https://www.jiosaavn.com/search/song/{query}"
        speak(f"Searching for {song_name} on JioSaavn.")
    else:
        # Generic fallback for other platforms
        url = f"https://www.{platform_match}.com/search/{query}"
        speak(f"Searching for {song_name} on {platform_match}.")

    print(f"🔗 Opening: {url}")
    webbrowser.open(url)


# ---------- Command Handler ----------
def play_song_from_command(command):
    command = command.lower()

    if "youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        play_on_youtube(song)

    elif "spotify" in command or "jiosaavn" in command or "saavn" in command:
        other_player(command)

    elif "on" in command:
        other_player(command)

    else:
        # Default fallback to YouTube
        song = command.replace("play", "").strip()
        play_on_youtube(song)
