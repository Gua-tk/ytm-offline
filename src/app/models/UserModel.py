#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

import bcrypt as bcrypt
from flask_login import UserMixin

from src.app.db import db


class UserModel(db.Model):
    email = db.Column(db.String(355), primary_key=True, unique=True)
    password = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = password  # bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        print("repr method")
        return f"<email {self.email}>"


