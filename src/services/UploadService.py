#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ytmusicapi
import os

class UploadService:
    def __init__(self):
        self.ytmusic = ytmusicapi.YTMusic("secrets/browser.json")

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