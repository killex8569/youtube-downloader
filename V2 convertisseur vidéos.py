import yt_dlp
import os

def download_video(url, output_folder):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Options to download the video in the highest quality available
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {'key': 'FFmpegMetadata'},  # Add metadata
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegThumbnailsConvertor', 'format': 'png'}  # Convert the thumbnail to PNG
            ],
            'writethumbnail': True,
            'prefer_ffmpeg': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'unnamed_video')
            thumbnail_path = os.path.join(output_folder, f"{title}.png")
            print(f"Download completed! Video: {title}")
            if os.path.exists(thumbnail_path):
                print(f"Thumbnail downloaded: {thumbnail_path}")
            else:
                print("Thumbnail not found or download failed.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the video URL: ")
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(parent_folder, 'video')
    download_video(url, output_folder)
