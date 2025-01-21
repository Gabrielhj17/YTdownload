#!/usr/bin/env python3

import yt_dlp
import os
import ssl
import sys

def download_video(url):
    try:
        # Get the user's Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Create SSL context that doesn't verify certificates
        ssl._create_default_https_context = ssl._create_unverified_context
        
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

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Usage: ytdownload [URL]")
        print("If no URL is provided, you will be prompted to enter one.")
        print("\nOptions:")
        print("  --help    Show this help message")
        sys.exit(0)
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube video URL: ")
    
    download_video(url)

if __name__ == "__main__":
    main()