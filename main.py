from pytube import Youtube

url = input('Enter a Video url to Download')
yt = Youtube(url)

audio_stream = yt.streams.filter(only_audio=True).firts()
audio_stream.download()