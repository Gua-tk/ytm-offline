#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt

from src.app.models.Video import Video
from src.app.extensions import db


class VideoService:
    def __init__(self):
        pass

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
