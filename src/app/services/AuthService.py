from src.app.db import db
from src.app.services.UserService import UserService


def verify_password(username, password):
    user_model = UserService().get_user(username)
    print("user model " + str(user_model))
    if user_model is not None and user_model.password.__eq__(password):
        return username


def get_password(username):
    password = db.get_user_password(username)
    print("the got password in get_password " + password)
    return password

