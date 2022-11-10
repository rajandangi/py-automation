import pytube
link = input('https://www.youtube.com/watch?v=AZTjWmRP5ak')
dn = pytube.YouTube(link)
dn.streams.first().download()
print('Your Video Has Been Downloaded', link)
