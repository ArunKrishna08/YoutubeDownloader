#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------
# Name              : YouTube Downloader
# Purpose           : YouTube Audio Downloader with GUI
# Author            : Arun K
# Version           : 1.4
# Last Modified     : 11/04/2017
# ----------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
import pafy

class YouTubeDownloader:
    def __init__(self,master):
        self.master = master
        master.title("Youtube Downloader")
        Label(master, text="YouTube URL:").grid(row=0)
        self.url_field = Entry(master)
        self.url_field.grid(row=0, column=1)
        Button(master, text='Paste URL', command=self.url).grid(row=0, column=4, sticky=W, pady=10)
        Button(master, text='Download Audio', command=self.download_audio).grid(row=12, column=1, sticky=W, pady=10)

    def url(self):
        url = self.url_field.get()
        self.data = pafy.new(url)

    def download_audio(self):
        best_audio = self.data.getbestaudio()
        best_audio.download(quiet = False)


root = Tk()
my_youtube = YouTubeDownloader(root)
root.mainloop()
