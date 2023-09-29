#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt
from yt_dlp.utils import ExtractorError

from src.app.models.Video import Video
from src.app.db import db


class YoutubeService:
    def __init__(self):
        pass

    def download_audio_playlist(self, url, output_directory, codec="mp3"):
        file_directory = self.get_playlist_title(url)
        with yt.YoutubeDL(self.audio_playlist_options(codec, output_directory)) as ydl:
            try:
                ydl.download([url])
            except ExtractorError as e:
                print("An error happened during the download of the audio " + url)
                print(e)

        return file_directory

    def download_playlist_data(self, playlist_url):
        # Extract information about the playlist
        # TODO this line fails if there is a private video in the playlist
        playlist_info = yt.YoutubeDL().extract_info(playlist_url, download=False)

        # Get playlist title and description
        return playlist_info.get('title', 'Untitled Playlist'), playlist_info.get('description',
                                                                                  'No description available')

    def get_playlist_title(self, url):
        info = yt.YoutubeDL().extract_info(url, download=False)
        return info.get('title', 'unknown_playlist')

    def download_audio(self, url, output_directory=".", codec="mp3"):
        file_name = self.get_video_title(url) + ".mp3"
        audio_options = self.audio_options(codec, output_directory)
        with yt.YoutubeDL(audio_options) as ydl:
            ydl.download([url])
        return file_name

    def get_video_title(self, url):
        info = yt.YoutubeDL().extract_info(url, download=False)
        return info.get('title', 'unknown_playlist')

    def audio_options(self, codec, output_directory):
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec,
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
        }

    # CRUD methods
    def get_all_videos(self):
        return Video.query.all()

    def get_video_by_id(self, book_id):
        return Video.query.get(book_id)

    def create_video(self, data):
        video = Video(**data)
        db.session.add(video)
        db.session.commit()
        return video

    def delete_video(self, video):
        db.session.delete(video)
        db.session.commit()

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
