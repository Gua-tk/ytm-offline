#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt


class DownloadService:
    def __init__(self):
        pass

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
        with yt.YoutubeDL(self.audio_options(codec, output_directory)) as ydl:
            ydl.download([url])

    def download_audio_playlist(self, url, output_directory=".", codec="mp3"):
        with yt.YoutubeDL(self.audio_playlist_options(codec, output_directory)) as ydl:
            ydl.download([url])
