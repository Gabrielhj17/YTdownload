#!/usr/bin/env python3

import yt_dlp
import os

def download_video(url):
    try:
        # Get the user's Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # yt-dlp options
        ydl_opts = {
            "format": "best",
            "outtmpl": f"{downloads_folder}/%(title)s.%(ext)s",  # Save to Downloads folder
            "quiet": False,  # Show progress
            "progress": True,
            "no_warnings": False
        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading to: {downloads_folder}")
            ydl.download([url])
        print("Download completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)