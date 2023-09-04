from flask import Flask

from src.app.controllers.video_routes import video_bp  # Import your blueprints

app = Flask(__name__)
app.config.from_object('src.app.config')

app.register_blueprint(video_bp)
