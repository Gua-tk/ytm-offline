#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt
import os
import ytmusicapi

from src.app.models.Playlist import Playlist
from src.app.extensions import db


class YoutubeMusicService:

    def __init__(self):
        absolute_current_file_path = os.path.abspath(__file__)
        absolute_services_path = os.path.dirname(absolute_current_file_path)
        absolute_app_path = os.path.dirname(absolute_services_path)
        absolute_src_path = os.path.dirname(absolute_app_path)
        absolute_project_path = os.path.dirname(absolute_src_path)

        token_absolute_path = os.path.join(absolute_project_path, "secrets/browser.json")
        headers_absolute_path = os.path.join(absolute_project_path, "secrets/headers.txt")

        if os.path.isfile(token_absolute_path):
            self.ytmusic = ytmusicapi.YTMusic(token_absolute_path)
        elif os.path.isfile(headers_absolute_path):
            ytmusicapi.setup(filepath=token_absolute_path, headers_raw="".join(open(headers_absolute_path).readlines()))
            self.ytmusic = ytmusicapi.YTMusic(token_absolute_path)

    def get_playlist_title(self, url):
        info = yt.YoutubeDL().extract_info(url, download=False)
        return info.get('title', 'unknown_playlist')

    def audio_playlist_options(self, codec, output_directory):
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

    def download_audio_playlist(self, url, output_directory=".", codec="mp3"):
        file_directory = self.get_playlist_title(url)
        with yt.YoutubeDL(self.audio_playlist_options(codec, output_directory)) as ydl:
            ydl.download([url])
        return file_directory

    def download_playlist_data(self, playlist_url):
        # Extract information about the playlist
        playlist_info = yt.YoutubeDL().extract_info(playlist_url, download=False)

        # Get playlist title and description
        return playlist_info.get('title', 'Untitled Playlist'), playlist_info.get('description',
                                                                                  'No description available')

    def upload_audio(self, audio_path):
        upload_info = self.ytmusic.upload_song(audio_path)
        return upload_info

    def upload_playlist(self, playlist_directory):
        upload_infos = []
        for filename in os.listdir(playlist_directory):
            file_path = os.path.join(playlist_directory, filename)
            print("UPLOADING " + filename)
            upload_infos.append(self.upload_audio(file_path))
        return upload_infos

    def create_playlist(self, playlist_title, playlist_description):
        response = self.ytmusic.create_playlist(playlist_title, playlist_description)
        return response['playlistId']

    def add_songs_to_playlist(self, playlist_id, video_ids):
        self.ytmusic.add_playlist_items(playlist_id, video_ids)

    # CRUD methods
    def get_all_playlists(self):
        return Playlist.query.all()

    def get_playlist_by_id(self, book_id):
        return Playlist.query.get(book_id)

    def save_playlist(self, data):
        playlist = Playlist(**data)
        db.session.add(playlist)
        db.session.commit()
        return playlist

    def delete_playlist(self, playlist):
        db.session.delete(playlist)
        db.session.commit()
