from flask import Blueprint
from flask_restx import Api, Resource, fields

from src.app.AppSingleton import auth
from src.app.services.YoutubeService import YoutubeService

youtube_bp = Blueprint('video', __name__, url_prefix='/api/youtube')
api = Api(youtube_bp, doc='/doc', title='Video REST API', version='1.0')

video_fields = api.model('Video', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a video in our db'),
    'name': fields.String(required=True, description='The video title'),
    'description': fields.String(description='A brief description of the video'),
    'URL': fields.String(required=True, description='Youtube URL to watch the video'),
})

youtubeService = YoutubeService()


@api.route('/')
class VideoList(Resource):
    @api.marshal_list_with(video_fields)
    @auth.login_required
    def get(self):
        """List all videos"""
        videos = youtubeService.get_all_videos()
        return videos

    @api.expect(video_fields)
    @api.marshal_with(video_fields, code=201)
    @auth.login_required
    def post(self):
        """Create a new video"""
        data = api.payload
        video = youtubeService.create_video(data)
        return video, 201


@api.route('/<int:id>')
@api.param('id', 'The video identifier')
@api.response(404, 'Video not found')
class VideoDetail(Resource):
    @api.marshal_with(video_fields)
    @auth.login_required
    def get(self, video_id):
        """Get a video by ID"""
        video = youtubeService.get_video_by_id(video_id)
        if video is None:
            api.abort(404, message="Video not found")
        return video

    @api.response(204, 'Video deleted')
    @auth.login_required
    def delete(self, video_id):
        """Delete a video by ID"""
        video = youtubeService.get_video_by_id(video_id)
        if video is None:
            api.abort(404, message="Video not found")
        youtubeService.delete_video(video)
        return '', 204
