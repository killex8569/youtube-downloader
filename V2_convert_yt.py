import yt_dlp
import os
import sys

def download_video(url, output_folder, cookies_path=None, download_playlist=True, embed_thumbnail=True):
    """
    Télécharge une vidéo ou playlist depuis YouTube avec gestion des cookies et multi-plateforme.
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        # Configuration yt-dlp
        postprocessors = [{'key': 'FFmpegMetadata'}]
        if embed_thumbnail:
            postprocessors.append({'key': 'EmbedThumbnail', 'already_have_thumbnail': False})

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': not download_playlist,
            'postprocessors': postprocessors,
            'writethumbnail': embed_thumbnail,
            'prefer_ffmpeg': True,
        }

        if cookies_path and os.path.exists(cookies_path):
            print(f"Using cookies from {cookies_path}")
            ydl_opts['cookiefile'] = cookies_path
        else:
            print("No cookies file found or invalid. Some videos may return HTTP 403 Forbidden.")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'unnamed_video')
            print(f"Download completed: {title}")

    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
        if "403" in str(e):
            print("HTTP 403 Forbidden: You may need a valid cookies.txt or the video may be age/region restricted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the video URL: ").strip()

    # Détermination du dossier de sortie selon l'OS
    home_folder = os.path.expanduser("~")
    if sys.platform == "win32":
        output_folder = os.path.join(home_folder, "Desktop", "yt-dl")
    else:
        output_folder = os.path.join(home_folder, "Vidéos", "yt-dl")

    # Détection automatique du fichier cookies.txt dans le dossier du script
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    cookies_path = os.path.join(parent_folder, 'cookies.txt')
    if not os.path.exists(cookies_path):
        cookies_path = None

    # Option pour télécharger la playlist ou juste la vidéo
    download_playlist = True
    choice = input("Do you want to download the full playlist if available? (y/N): ").strip().lower()
    if choice != 'y':
        download_playlist = False

    # Option pour embed thumbnails (True = embed, False = ignorer pour éviter les erreurs)
    embed_thumbnail = True
    choice_thumb = input("Do you want to embed video thumbnails? (Y/n): ").strip().lower()
    if choice_thumb == 'n':
        embed_thumbnail = False

    download_video(url, output_folder, cookies_path, download_playlist, embed_thumbnail)
