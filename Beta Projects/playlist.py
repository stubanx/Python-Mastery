from pytube import Playlist
import os

# Specify the playlist URL and download directory
playlist_url = "https://youtube.com/playlist?list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt&si=FpgrbGIPPKF_9GT-"
download_directory = "C:\Users\nites\OneDrive\Documents\NPTEL\vids"

# Create Playlist object
playlist = Playlist(playlist_url)

# Ensure the directory exists
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Iterate through each video in the playlist
print(f"Starting download for playlist: {playlist.title}")
for video in playlist.videos:
    # print(f"Downloading: {video.title}")
    video.streams.get_highest_resolution().download(download_directory)
    print(f"Downloaded:")


print("All videos downloaded successfully!")
