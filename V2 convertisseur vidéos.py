import yt_dlp
import os

def download_video(url, output_folder, cookies_path):
    try:
        # Créez le dossier si nécessaire
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Options pour yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {'key': 'FFmpegMetadata'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegThumbnailsConvertor', 'format': 'png'}
            ],
            'writethumbnail': True,
            'prefer_ffmpeg': True,
            'cookiefile': cookies_path  # Utilisation des cookies
        }

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
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(parent_folder, 'video')
    cookies_path = os.path.join(parent_folder, 'cookies.txt')

    if os.path.exists(cookies_path):
        print(f"Using cookies from {cookies_path}")
    else:
        print("Cookies file not found. Please export cookies as cookies.txt")

    download_video(url, output_folder, cookies_path)
