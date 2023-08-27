#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from flask import Flask, request, jsonify, send_file

from src.services.DownloadService import DownloadService
from src.services.CompressionService import CompressionService
import os

app = Flask(__name__)
ds = DownloadService()
cs = CompressionService()

download_path = os.path.join(os.path.dirname(os.path.dirname(app.root_path)), "downloads")


'''# Read all
@app.route('/playlist/<str:playlist_url>', methods=['POST'])
def get_items():
    return jsonify(items), 200'''
# https://youtube.com/playlist?list=PLvEI0iOxif017-fv4P0ApFmzRI-vWBPvb&si=BmAWXxAFVAa_gg86
@app.route('/playlist', methods=['POST'])
def download_playlist():
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    ds.download_audio_playlist(playlist_url, current_download_path)
    directory_name = ds.get_playlist_title(playlist_url)
    cs.zip_folder(os.path.join(current_download_path, directory_name), os.path.join(current_download_path, directory_name + ".zip"))
    return send_file(os.path.join(current_download_path, directory_name + ".zip"), as_attachment=True)


@app.route('/audio', methods=['POST'])
def download_audio():
    data = request.json
    audio_url = data['audio_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "audios", str(request_uuid))
    ds.download_audio(audio_url, current_download_path)
    file_name = ds.get_playlist_title(audio_url) + ".mp3"
    return send_file(os.path.join(current_download_path, file_name), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)