from pytube import YouTube


while True:
    while True:
        input_link = input('Enter Link of the video: ')

        try:
            link = YouTube(input_link)
            break
        except:
            print('Connection Error, Try again.')
            

    print('\nEnter Format')
    print('1. Video Format')
    print('2. Audio Format')

    frmt = int(input('\nChoose Format: '))

    try:
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

           
            strt = input('Whould you like to download another video?(y/n): ')
            if strt == 'n' or strt == 'N':
                break
            elif strt == 'y' or 'Y':
                pass

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

            strt = input('Whould you like to download another video?(y/n): ')
            if strt == 'n' or strt == 'N':
                break
            elif strt == 'y' or 'Y':
                pass

    except:
        print('Video not found, Try again\n')
