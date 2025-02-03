from pytube import YouTube


url = "https://www.youtube.com/watch?v=QXJStWTZf9w&ab_channel=MovieClips"

yt = YouTube(url)

print(yt.title)
# video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# video.download(output_path="h:/Downloads")