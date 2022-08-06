from pytube import YouTube


input_link = input('Enter Link of the video: ')

try:
    link = YouTube(input_link)
except:
    print('Connection Error')
    quit()

print('\nEnter Format')
print('1. Video Format')
print('2. Audio Format')

frmt = int(input('\nChoose Format: '))
print('\nLoading available resolutions...\n')

if frmt == 1:
    videos = link.streams.filter(file_extension='mp4')
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input('Choose Resulotion (0,1,2,...): '))
    ttle = link.title
    print('\nDownloading...')
    videos[strm].download()
    print('Download Completed. ',"\"", ttle, "\"")

elif frmt == 2:
    videos = link.streams.filter(only_audio=True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input('Choose Resulotion (0,1,2,...): '))
    ttle = link.title
    print('\nDownloading...',)
    videos[strm].download()
    print('Download Completed. ',"\"", ttle, "\"")