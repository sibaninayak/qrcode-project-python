from pytube import YouTube
yt = YouTube("https://youtu.be/aqW4xXUgmno")
yt.streams.filter(progressive = True , file_extension='mp4').order_by(
    'resolution').desc().first().download()