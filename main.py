from pytube import YouTube
import moviepy.editor as mp
import os
import tkinter as tk
from tkinter.filedialog import askopenfile, askdirectory

def remove(directory, name):
    full_path = directory + name + '.mp4'
    os.remove(full_path)

def download(song, directory):
    try:
        yt = YouTube(song)
        audio = yt.streams.first()
        audio.download(output_path = directory)
        clip = mp.VideoFileClip(directory + yt.title + '.mp4')
        clip.audio.write_audiofile(directory + yt.title + '.mp3')
        remove(directory, yt.title)
    except:
        open('failed.txt', 'a').write(song + '\n')
    
def main():
    songs = []
    
    songs_list = askopenfile(mode='r').name
    with open(songs_list, 'r') as f:
        for song in f.readlines():
            song.strip()
            songs.append(song)
    directory = askdirectory()
    for song in songs:
        download(song, directory + '/')

if __name__ == "__main__":
    main()