#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, request
from flask_restx import Api, fields

from src.app.services.UserService import UserService

user_bp = Blueprint('user', __name__, url_prefix='/api/user')
api = Api(user_bp, doc='/doc', title='Playlist REST API', version='1.0')

user_fields = api.model('User', {
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='The password of the user'),
})

userService = UserService()


@user_bp.route('/signup', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    user_model = userService.get_user(email)
    if user_model is not None:
        return "User with email " + email + " already exists in the database\n", 400
    userService.create_user(email, password)
    return "User created", 200


@user_bp.route('/login', methods=['POST'])
def log_in():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    print("LOG IN EMAIL:\t", email)
    print("LOG IN PASSWORD:\t", password)
    user_model = userService.get_user(email)
    if user_model is None:
        return "User with email " + email + " does not exist in the database\n", 404
    elif user_model.password.__eq__(password):
        # TODO implement authentication for the front-end
        return "Logged in\n", 200
    else:
        return "Incorrect password\n", 404
