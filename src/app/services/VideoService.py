#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yt_dlp as yt

from src.app.models.Video import Video
from src.app.extensions import db


def get_all_videos():
    return Video.query.all()


def get_video_by_id(book_id):
    return Video.query.get(book_id)


def create_video(data):
    video = Video(**data)
    db.session.add(video)
    db.session.commit()
    return video


def delete_video(video):
    db.session.delete(video)
    db.session.commit()


def download_audio(self, url, output_directory=".", codec="mp3"):
    file_name = self.get_playlist_title(url) + ".mp3"
    audio_options = self.audio_options(codec, output_directory)
    with yt.YoutubeDL(audio_options) as ydl:
        ydl.download([url])
    return file_name
