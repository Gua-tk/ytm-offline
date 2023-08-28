#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ytmusicapi
import os

class UploadService:
    def __init__(self):
        print("CURRENT PATH:" + str(os.getcwd()))

        absolute_current_file_path = os.path.abspath(__file__)

        absolute_services_path = os.path.dirname(absolute_current_file_path)

        absolute_src_path = os.path.dirname(absolute_services_path)

        absolute_project_path = os.path.dirname(absolute_src_path)
        token_absolute_path = os.path.join(absolute_project_path, "secrets/browser.json")
        headers_absolute_path = os.path.join(absolute_project_path, "secrets/headers.txt")

        if os.path.isfile(token_absolute_path):
            self.ytmusic = ytmusicapi.YTMusic(token_absolute_path)
        elif os.path.isfile(headers_absolute_path):
            ytmusicapi.setup(filepath=token_absolute_path, headers_raw="".join(open(headers_absolute_path).readlines()))
            self.ytmusic = ytmusicapi.YTMusic(token_absolute_path)

        with open("fast", "w+") as t:
            t.write("olsaaaa")

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