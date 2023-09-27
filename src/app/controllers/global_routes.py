#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import os

from flask import Blueprint
from flask import request, send_file
from flask_restx import Api, Resource

from src.app.services.YoutubeMusicService import YoutubeMusicService
from src.app.services.YoutubeService import YoutubeService
from src.app.services.CompressionService import CompressionService

global_bp = Blueprint('global', __name__, url_prefix='/api/global')
api = Api(global_bp, doc='/doc', title='Global REST API', version='1.0')

videoService = YoutubeService()
compressionService = CompressionService()
playlistService = YoutubeMusicService()

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
download_path = os.path.join(root_path, "downloads")


@global_bp.route('/downloadPlaylist', methods=['POST'])
def download_playlist():
    """
    Downloads a playlist from youtube as a set of .mp3 files compressed into a single .zip file.
    :return: a .zip file containing all the .mp3 files of the supplied playlist.
    """
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    directory_name = videoService.download_audio_playlist(playlist_url, current_download_path)
    print("Directory name for playlist is " + directory_name)
    compressionService.zip_folder(os.path.join(current_download_path, directory_name),
                                  os.path.join(current_download_path, directory_name + ".zip"))
    return send_file(os.path.join(current_download_path, directory_name + ".zip"), as_attachment=True)


@global_bp.route('/downloadAudio', methods=['POST'])
def download_audio():
    data = request.json
    audio_url = data['audio_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "audios", str(request_uuid))
    file_name = videoService.download_audio(audio_url, current_download_path)
    return send_file(os.path.join(current_download_path, file_name), as_attachment=True)


@global_bp.route('/uploadAudio', methods=['POST'])
def upload_audio():
    data = request.json
    audio_url = data['audio_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "audios", str(request_uuid))
    file_name = videoService.download_audio(audio_url, current_download_path)
    return str(playlistService.upload_audio(os.path.join(current_download_path, file_name)))


@global_bp.route('/uploadPlaylist', methods=['POST'])
def upload_playlist():
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    directory_name = videoService.download_audio_playlist(playlist_url, current_download_path)
    print("DOWNLOADING FINISHED. STARTING UPLOAD<")
    upload_infos = playlistService.upload_playlist(os.path.join(current_download_path, directory_name))
    return "".join(str(upload_infos)) + "\n"


@global_bp.route('/uploadReceivedAudio', methods=['POST'])
def upload_received_audio():
    if 'file' not in request.files:
        abort(400)

    uploaded_file = request.files['file']
    print(uploaded_file.filename)


@global_bp.route('/uploadToPlaylist', methods=['POST'])
def upload_to_playlist():
    data = request.json
    playlist_url = data['playlist_url']
    request_uuid = uuid.uuid4()
    current_download_path = os.path.join(download_path, "playlists", str(request_uuid))
    directory_name = playlistService.download_audio_playlist(playlist_url, current_download_path)
    upload_infos = playlistService.upload_playlist(os.path.join(current_download_path, directory_name))
    title, description = playlistService.download_playlist_data(playlist_url)
    playlistService.save_playlist({'title': title, 'description': description})


@global_bp.route('/hello', methods=['GET'])
def hello():
    return 'hello world\n'
