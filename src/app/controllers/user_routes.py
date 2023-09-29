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
    userService.create_user(data["email"], data["password"])
    return "DONE", 201


@user_bp.route('/login', methods=['POST'])
def log_in():
    data = request.get_json()
    print("LOG IN EMAIL:\t", data["email"])
    print("LOG IN PASSWORD:\t", data["password"])
    userService.query_filter_by_email(data["email"], data["password"])
    return "DONE", 201

