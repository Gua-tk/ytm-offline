#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.app.extensions import db
from uuid import uuid4


def create_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, default=create_uuid())
    email = db.Column(db.String(355), unique=True)
    password = db.Column(db.String(), nullable=False)
