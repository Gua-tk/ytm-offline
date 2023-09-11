from flask import Blueprint
from flask_restx import Api, Resource, fields
from src.app.services.YoutubeService import YoutubeService

video_bp = Blueprint('video', __name__, url_prefix='/video')
api = Api(video_bp, doc='/doc', title='Video REST API', version='1.0')

video_fields = api.model('Video', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a video in our db'),
    'name': fields.String(required=True, description='The video title'),
    'description': fields.String(description='A brief description of the video'),
    'URL': fields.String(required=True, description='Youtube URL to watch the video'),
})

videoService = YoutubeService()


@api.route('/')
class VideoList(Resource):
    @api.marshal_list_with(video_fields)
    def get(self):
        """List all videos"""
        videos = videoService.get_all_videos()
        return videos

    @api.expect(video_fields)
    @api.marshal_with(video_fields, code=201)
    def post(self):
        """Create a new video"""
        data = api.payload
        video = videoService.create_video(data)
        return video, 201


@api.route('/<int:id>')
@api.param('id', 'The video identifier')
@api.response(404, 'Video not found')
class VideoDetail(Resource):
    @api.marshal_with(video_fields)
    def get(self, video_id):
        """Get a video by ID"""
        video = videoService.get_video_by_id(video_id)
        if video is None:
            api.abort(404, message="Video not found")
        return video

    @api.response(204, 'Video deleted')
    def delete(self, video_id):
        """Delete a video by ID"""
        video = videoService.get_video_by_id(video_id)
        if video is None:
            api.abort(404, message="Video not found")
        videoService.delete_video(video)
        return '', 204
