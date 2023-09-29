from src.app.db import db
from src.app.models.UserModel import UserModel


class UserService:
    def __init__(self):
        pass

    def create_user(self, email, password):
        user = UserModel(email=email, password=password)
        db.session.add(user)
        db.session.commit()

    def query_filter_by_email(self, email, password):
        user = UserModel.query.filter_by(email=email).first()
        if user is None:
            return 401

        if user.password != password:
            return 401
