from src.app.controllers.youtube_routes import youtube_bp
from src.app.controllers.youtube_music_routes import youtubeMusic_bp
from src.app.controllers.global_routes import global_bp
from src.app.controllers.user_routes import user_bp
from src.app.AppSingleton import app

app.register_blueprint(youtube_bp)
app.register_blueprint(youtubeMusic_bp)
app.register_blueprint(global_bp)
app.register_blueprint(user_bp)


