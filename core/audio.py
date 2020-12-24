from pafy import new
url = input("Enter the link: ")
video = new(url)
audio = video.audiostreams
audio[0].download()