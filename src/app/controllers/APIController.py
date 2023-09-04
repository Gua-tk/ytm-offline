#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from flask import Flask, request, send_file
import os
from flask_restx import Api

from src.app.services.YTMusicService import YTMusicService
from src.app.services.DownloadService import DownloadService
from src.app.services.CompressionService import CompressionService

app = Flask(__name__)  # Initialize Flask app
api = Api(app, doc='/swagger/')  # Specify the path to Swagger UI documentation

ds = DownloadService()
cs = CompressionService()
us = YTMusicService()

download_path = os.path.join(os.path.dirname(os.path.dirname(app.root_path)), "downloads")


# https://youtube.com/playlist?list=PLvEI0iOxif017-fv4P0ApFmzRI-vWBPvb&si=BmAWXxAFVAa_gg86
@app.route('/playlist', methods=['POST'])
@api.doc(params={'name': 'The name to greet'})
def download_playlist():
    """
    Downloads a playlist from youtube as a set of .mp3 files compressed into a single .zip file.
    :return: a .zip file containing all the .mp3 files of the supplied playlist.
    """
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


@app.route('/playlist/upload_to_playlist', methods=['POST'])
def upload_to_playlist():
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    directory_name = ds.download_audio_playlist(playlist_url, current_download_path)
    print("DOWNLOADING FINISHED. STARTING UPLOAD<")
    upload_infos = us.upload_playlist(os.path.join(current_download_path, directory_name))
    title, description = ds.download_playlist_data(playlist_url)
    us.create_playlist(title, description)


@app.route('/', methods=['GET'])
def hello():
    return 'Holaaaa MAMAMAA'



