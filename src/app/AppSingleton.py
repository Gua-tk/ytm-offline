#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth

from src.app.db import db
from src.app.services.AuthService import verify_password

app = Flask(__name__)
app.config.from_object('src.app.config')

# Initialize database config
db.init_app(app)

#  This allows us to use the server without having it online
with app.app_context():
    db.create_all()

'''
login_manager = LoginManager()
login_manager.init_app(app)
# The value refers to the function name that will handle the login process.
login_manager.login_view = "services.UserService.login"
login_manager.login_message_category = "danger"
'''
auth = HTTPBasicAuth()
auth.verify_password_callback = verify_password



