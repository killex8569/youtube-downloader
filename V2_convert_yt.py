import yt_dlp
import os
import sys

def download_video(url, output_folder, cookies_path=None):

    try:
        os.makedirs(output_folder, exist_ok=True)

        # Configuration yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': False,  # True pour télécharger seulement la vidéo, False pour playlist (idée d'update future)
            'postprocessors': [
                {'key': 'FFmpegMetadata'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegThumbnailsConvertor', 'format': 'png'}
            ],
            'writethumbnail': True,
            'prefer_ffmpeg': True,
        }

        # Ajouter les cookies que si le fichier existe
        if cookies_path and os.path.exists(cookies_path):
            print(f"Using cookies from {cookies_path}")
            ydl_opts['cookiefile'] = cookies_path
        else:
            print("No cookies file found, continuing without it...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'unnamed_video')
            print(f"Download completed! Video: {title}")

    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the video URL: ")

    # Déterminer le dossier utilisateur selon l'OS
    home_folder = os.path.expanduser("~")
    if sys.platform == "win32":
        output_folder = os.path.join(home_folder, "Desktop", "yt-dl")
    else:
        output_folder = os.path.join(home_folder, "Videos", "yt-dl")

    # Détection automatique du fichier cookies.txt dans le dossier du script
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    cookies_path = os.path.join(parent_folder, 'cookies.txt')
    if not os.path.exists(cookies_path):
        cookies_path = None  # Téléchargement sans cookies

    download_video(url, output_folder, cookies_path)
