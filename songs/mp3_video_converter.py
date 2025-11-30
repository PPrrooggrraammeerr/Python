
# coding: UTF-8

# mp3_video_converter.py

import yt_dlp
import os
import time
import shutil

get_cwd = os.getcwd ()

FFMPEG_PATH = r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin\ffmpeg.exe'

def find_video (music_name):

    ydl_opts = {
    
        'quiet': True,
        'extractaudio': True,
        'audioquality': 1,
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        
        'postprocessors': [{
        
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            
        }],
        
        'ffmpeg_location': FFMPEG_PATH
    }
    
    with yt_dlp.YoutubeDL (ydl_opts) as ydl:

        result = ydl.extract_info (f'ytsearch: {music_name}', download=False)

        if 'entries' in result:
        
            video_url = result ['entries'][0]['url']
            print (f'found video: {video_url}')
            return video_url
        
        else:
        
            print ('not found video...')
            return None

def download_youtube_for_mp3 (url, destination = 'audio.mp3'):

    ydl_opts = {
    
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        
        'postprocessors': [{
        
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
            
        }],
        
        'ffmpeg_location': FFMPEG_PATH
        
    }

    with yt_dlp.YoutubeDL (ydl_opts) as ydl:
    
        ydl.download ([url])

    for file in os.listdir ():
    
        if file.startswith ('temp_audio') and file.endswith ('.mp3'):
        
            os.rename (file, destination)
            
            print (f'Download completed!')
            return

    print ('Error: file MP3 not found!')

filename_songs = f'{get_cwd}\\songs.txt'

join_file = os.path.join (get_cwd, 'songs.txt')

file = open (f'{join_file}', 'r')

for song in file:

    columns = song.strip ().split (' - ')
    
    if len (columns) > 1:
        
        band_name = columns [0]
        file_join_band_name = os.path.join (get_cwd, band_name)
        
        os.mkdir (file_join_band_name)
    
        music_name = columns [1]
        file_join_music_name = os.path.join (file_join_band_name, music_name)
        
        os.mkdir (file_join_music_name)

        song = song.strip ()

        name_music = song
        url_video = find_video (name_music)

        if url_video:

            download_youtube_for_mp3 (url_video, f'{song}.mp3')
            time.sleep (3.5)
            
            shutil.move (f'{get_cwd}\\{song}.mp3', f'{get_cwd}\\{band_name}\\{music_name}\\{song}.mp3')

