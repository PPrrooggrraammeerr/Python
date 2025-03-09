
# coding: UTF-8

# mp3_video_converter.py

import yt_dlp
import os

get_cwd = os.getcwd ()

FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe'

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
    
with open (filename_songs, 'r') as file:

    songs = file.readlines ()

    for song in songs:

        song = song.strip ()

        name_music = song
        url_video = find_video (name_music)

        if url_video:

            download_youtube_for_mp3 (url_video, f'{song}.mp3')

