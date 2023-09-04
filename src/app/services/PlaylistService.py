#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt
import os
import ytmusicapi

absolute_current_file_path = os.path.abspath(__file__)
absolute_services_path = os.path.dirname(absolute_current_file_path)
absolute_app_path = os.path.dirname(absolute_services_path)
absolute_src_path = os.path.dirname(absolute_app_path)
absolute_project_path = os.path.dirname(absolute_src_path)

token_absolute_path = os.path.join(absolute_project_path, "secrets/browser.json")
headers_absolute_path = os.path.join(absolute_project_path, "secrets/headers.txt")

if os.path.isfile(token_absolute_path):
    ytmusic = ytmusicapi.YTMusic(token_absolute_path)
elif os.path.isfile(headers_absolute_path):
    ytmusicapi.setup(filepath=token_absolute_path, headers_raw="".join(open(headers_absolute_path).readlines()))
    ytmusic = ytmusicapi.YTMusic(token_absolute_path)

with open("fast", "w+") as t:
    t.write("olsaaaa")


def get_playlist_title(url):
    info = yt.YoutubeDL().extract_info(url, download=False)
    return info.get('title', 'unknown_playlist')


def audio_options(codec, output_directory):
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
    }


def audio_playlist_options(codec, output_directory):
    return {
        'yes_playlist': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_directory}/%(playlist_title)s/%(title)s.%(ext)s',
    }


def download_audio_playlist(url, output_directory=".", codec="mp3"):
    file_directory = get_playlist_title(url)
    with yt.YoutubeDL(audio_playlist_options(codec, output_directory)) as ydl:
        ydl.download([url])
    return file_directory


def download_playlist_data(playlist_url):
    # Extract information about the playlist
    playlist_info = yt.YoutubeDL().extract_info(playlist_url, download=False)

    # Get playlist title and description
    return playlist_info.get('title', 'Untitled Playlist'), playlist_info.get('description', 'No description available')


def upload_audio(audio_path):
    upload_info = ytmusic.upload_song(audio_path)
    return upload_info


def upload_playlist(playlist_directory):
    upload_infos = []
    for filename in os.listdir(playlist_directory):
        file_path = os.path.join(playlist_directory, filename)
        print("UPLOADING " + filename)
        upload_infos.append(upload_audio(file_path))
    return upload_infos


def create_playlist(playlist_title, playlist_description):
    response = ytmusic.create_playlist(playlist_title, playlist_description)
    return response['playlistId']


def add_songs_to_playlist(playlist_id, video_ids):
    ytmusic.add_playlist_items(playlist_id, video_ids)
