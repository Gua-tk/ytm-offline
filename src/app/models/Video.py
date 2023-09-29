from src.app.db import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    URL = db.Column(db.String(1000), nullable=False)
