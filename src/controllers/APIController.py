#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from flask import Flask, request, jsonify, send_file
import os

from src.services.UploadService import UploadService
from src.services.DownloadService import DownloadService
from src.services.CompressionService import CompressionService

app = Flask(__name__)
ds = DownloadService()
cs = CompressionService()
us = UploadService()

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
    directory_name = ds.download_audio_playlist(playlist_url, current_download_path)
    cs.zip_folder(os.path.join(current_download_path, directory_name), os.path.join(current_download_path, directory_name + ".zip"))
    return send_file(os.path.join(current_download_path, directory_name + ".zip"), as_attachment=True)


@app.route('/audio', methods=['POST'])
def download_audio():
    data = request.json
    audio_url = data['audio_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "audios", str(request_uuid))
    file_name = ds.download_audio(audio_url, current_download_path)
    return send_file(os.path.join(current_download_path, file_name), as_attachment=True)


@app.route('/audio/upload', methods=['POST'])
def upload_audio():
    data = request.json
    audio_url = data['audio_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "audios", str(request_uuid))
    file_name = ds.download_audio(audio_url, current_download_path)
    return str(us.upload_audio(os.path.join(current_download_path, file_name)))


@app.route('/playlist/upload', methods=['POST'])
def upload_playlist():
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    directory_name = ds.download_audio_playlist(playlist_url, current_download_path)
    print("DOWNLOADING FINISHED. STARTING UPLOAD<")
    upload_infos = us.upload_playlist(os.path.join(current_download_path, directory_name))
    return "\n".join(upload_infos)


@app.route('/', methods=['GET'])
def hello():
    return 'Holaaaa MAMAMAA'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
