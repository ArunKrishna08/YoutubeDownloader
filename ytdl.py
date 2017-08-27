#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------
# Name              : YouTube Downloader
# Purpose           : YouTube Audio/Video Downloader
# Author            : Arun K
# Email id          : akarunkrishna08@gmail.com
# Version           : 1.1
# Last Modified     : 21/08/2017
# ----------------------------------------------------------------------------------------------------------------------

'''
   NOTE:
 ------------
                       1) Before running this code, Please Install Python Package Manager
                                         "sudo apt-get install python-pip"

                       2) Please append "sudo" when running the code for the first time
                                           "sudo python ytdl.py"
'''


# Import System Module
import sys
# Import Python Package Manager
import pip
# Import Time Module
import time

print("")
print("*************************    ********************************")
print("**********************         ******************************")
print("********************             ****************************")
print("*****************                   *************************")
print("**************    Life is Short!!!!    **********************")
print("************  You Definitely Need Python  *******************")
print("*********                                   *****************")
print("*******                                       ***************")
print("")
print("*************************************************************")

PY_VERSION = sys.version_info[0]

# python package installer
def install(package):
    pip.main(['install', package])

if PY_VERSION == 3:

    try:
        # Import YouTube-dl Module
        import youtube_dl

    except ImportError:
        print("")
        print("YouTube-dl Module is not installed, Installing it now...")
        print("")
        install('youtube-dl')

    try:
        # Import Pafy Module
        import pafy

    except ImportError:
        print("")
        print("Pafy Module is not installed, Installing it now...")
        print("")
        install('pafy')
        import pafy

    flag = 0
    print("")
    print("")
    print(" +-------------------------------------------------+")
    print(" |                                                 |")
    print(" |   *****/ Welcome to YouTube Downloader /*****   |")
    print(" |                                                 |")
    print(" +-------------------------------------------------+")
    print("")
    print("")
    url = input("Please paste YouTube URL: " )
    video_count = 1
    audio_count =1
    print("")
    media = pafy.new(url)
    print("Author       : "+media.author)
    print("Title        : "+media.title)
    print("Duration     : "+media.duration)
    print("Published on : "+media.published)
    print("")
    A_V = int(input("Hit 1 to download Audio \n    2 to download Video File!\n  :"))

    if A_V == 1:
        print("")
        for audio_streams in media.audiostreams:
            print(audio_count, audio_streams.bitrate, audio_streams.extension)
            audio_count += 1
        audio_index = int(input(" Please select the Audio Quality: "))
        time.sleep(0.8)
        print(" Your audio file will start downloading now... ")
        media.audiostreams[audio_index-1].download(quiet=False)
        print(" /*** Downdload has been completed ***/")
        print("")
        print(" See you soon baby ;-)) ")
        print("")
        print("-" * 50)

    elif A_V == 2:
        print("")
        for video_streams in media.streams:
            print(video_count, video_streams.resolution, video_streams.extension)
            video_count += 1
        print("")
        video_index = int(input(" Please select the Video Quality: "))
        print("")
        time.sleep(0.8)
        print(" Your video file will start downloading now... ")
        media.streams[video_index-1].download(quiet=False)
        print(" /*** Downdload has been completed ***/")
        print("")
        print(" See you soon baby ;-)) ")
        print("")
        print("-" * 50)

    else:
        print(" Please enter VALID input!!!")

elif PY_VERSION == 2:
    try:
        # Import YouTube-dl Module
        import youtube_dl

    except ImportError:
        print("")
        print("YouTube-dl Module is not installed, Installing it now...")
        print("")
        install('youtube-dl')

    try:
        # Import Pafy Module
        import pafy

    except ImportError:
        print("")
        print("Pafy Module is not installed, Installing it now...")
        print("")
        install('pafy')
        import pafy

    flag = 0
    print("*" * 50)
    print("")
    print("")
    print(" +-------------------------------------------------+")
    print(" |                                                 |")
    print(" |   *****/ Welcome to YouTube Downloader /*****   |")
    print(" |                                                 |")
    print(" +-------------------------------------------------+")
    print("")
    print("")
    url = raw_input("Please paste YouTube URL: " )
    video_count = 1
    audio_count =1
    print("")
    media = pafy.new(url)
    print("Author       : "+media.author)
    print("Title        : "+media.title)
    print("Duration     : "+media.duration)
    print("Published on : "+media.published)
    print("")
    A_V = int(raw_input("Hit 1 to download Audio \n    2 to download Video File!\n  :"))

    if A_V == 1:
        print("")
        for audio_streams in media.audiostreams:
            print(audio_count, audio_streams.bitrate, audio_streams.extension)
            audio_count += 1
        audio_index = int(raw_input(" Please select the Audio Quality: "))
        time.sleep(0.8)
        print(" Your audio file will start downloading now... ")
        media.audiostreams[audio_index-1].download(quiet=False)
        print(" /*** Downdload has been completed ***/")
        print("")
        print(" See you soon baby ;-)) ")
        print("")
        print("-" * 50)

    elif A_V == 2:
        print("")
        for video_streams in media.streams:
            print(video_count, video_streams.resolution, video_streams.extension)
            video_count += 1
        print("")
        video_index = int(raw_input(" Please select the Video Quality: "))
        print("")
        time.sleep(0.8)
        print(" Your video file will start downloading now... ")
        media.streams[video_index-1].download(quiet=False)
        print(" /*** Downdload has been completed ***/")
        print("")
        print(" See you soon baby ;-)) ")
        print("")
        print("-" * 50)

    else:
        print(" Please enter VALID input!!!")
