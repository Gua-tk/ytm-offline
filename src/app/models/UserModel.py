#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.app.db import db
from uuid import uuid4

'''
def create_uuid():
    return uuid4().hex
'''


class UserModel(db.Model):
    # id = db.Column(db.String(32), primary_key=True, default=create_uuid())
    email = db.Column(db.String(355), primary_key=True, unique=True)
    password = db.Column(db.String(), nullable=False)
