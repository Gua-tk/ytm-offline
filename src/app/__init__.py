from src.app.controllers.video_routes import video_bp
from src.app.controllers.playlist_routes import playlist_bp
from src.app.controllers.global_routes import global_bp
from src.app.AppSingleton import app

app.register_blueprint(video_bp)
app.register_blueprint(playlist_bp)
app.register_blueprint(global_bp)


