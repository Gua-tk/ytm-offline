#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from src.app.db import db

app = Flask(__name__)
app.config.from_object('src.app.config')

# Initialize database config
db.init_app(app)

#  This allows us to use the server without having it online
with app.app_context():
    db.create_all()

