#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt


class DownloadService:
    def __init__(self):
        pass

    def get_playlist_title(self, url):
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

    def download_audio(self, url, output_directory=".", codec="mp3"):
        file_name = self.get_playlist_title(url) + ".mp3"
        audio_options = self.audio_options(codec, output_directory)
        with yt.YoutubeDL(audio_options) as ydl:
            ydl.download([url])
        return file_name


    def download_audio_playlist(self, url, output_directory=".", codec="mp3"):
        file_directory = self.get_playlist_title(url)
        with yt.YoutubeDL(self.audio_playlist_options(codec, output_directory)) as ydl:
            ydl.download([url])
        return file_directory