#!/usr/bin/env python
# -*- coding: utf-8 -*-
SWAGGER = {
    'title': 'YTM offline API',
    'uiversion': 3,
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"
