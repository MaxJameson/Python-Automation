from pytube import YouTube
from sys import argv

# takes argument from command line and stores it
link = argv[1]
yt = YouTube(link)

print("Downloading: ", yt.title)

# fetches video stream
yd = yt.streams.get_highest_resolution()

# downloads video to device
yd.download('./Downloads')

print("Video downloaded")



