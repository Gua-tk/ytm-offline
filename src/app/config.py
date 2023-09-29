#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

SWAGGER = {
    'title': 'YTM offline API',
    'uiversion': 3,
}

postgres_username = os.environ.get("POSTGRES_USERNAME")

if postgres_username is None:
    postgres_username = "ytm"

postgres_password = os.environ.get("POSTGRES_PASSWORD")

if postgres_password is None:
    postgres_password = "changeit"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "postgresql://" + postgres_username + ":" + postgres_password + "@postgres-db:5432" \
                                                                                           "/ytm_backend"

print("url" + SQLALCHEMY_DATABASE_URI)
# r"sqlite:///./db.sqlite "


