from flask import Blueprint
from flask_restx import Api, Resource, fields
from src.app.services.YoutubeMusicService import YoutubeMusicService

youtubeMusic_bp = Blueprint('playlist', __name__, url_prefix='/api/youtube_music')
api = Api(youtubeMusic_bp, doc='/doc', title='Playlist REST API', version='1.0')

playlist_fields = api.model('Playlist', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a playlist in our db'),
    'name': fields.String(required=True, description='The playlist title'),
    'description': fields.String(description='A brief description of the playlist'),
    'URL': fields.String(required=True, description='Youtube URL to watch the playlist'),
})

youtubeMusicService = YoutubeMusicService()


@api.route('/')
class PlaylistList(Resource):
    @api.marshal_list_with(playlist_fields)
    def get(self):
        """List all playlists"""
        playlists = youtubeMusicService.get_all_playlists()
        return playlists

    @api.expect(playlist_fields)
    @api.marshal_with(playlist_fields, code=201)
    def post(self):
        """Create a new playlist"""
        data = api.payload
        playlist = youtubeMusicService.save_playlist(data)
        return playlist, 201


@api.route('/<int:id>')
@api.param('id', 'The playlist identifier')
@api.response(404, 'Playlist not found')
class PlaylistDetail(Resource):
    @api.marshal_with(playlist_fields)
    def get(self, playlist_id):
        """Get a playlist by ID"""
        playlist = youtubeMusicService.get_playlist_by_id(playlist_id)
        if playlist is None:
            api.abort(404, message="Playlist not found")
        return playlist

    @api.response(204, 'Playlist deleted')
    def delete(self, playlist_id):
        """Delete a playlist by ID"""
        playlist = youtubeMusicService.get_playlist_by_id(playlist_id)
        if playlist is None:
            api.abort(404, message="Playlist not found")
        youtubeMusicService.delete_playlist(playlist)
        return '', 204
