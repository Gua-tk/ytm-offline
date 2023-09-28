from src.app.extensions import db
from src.app.models.User import User


class UserService:
    def __init__(self):
        pass

    def create_user(self, email, password):
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

    def query_filter_by_email(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user is None:
            return 401

        if user.password != password:
            return 401
