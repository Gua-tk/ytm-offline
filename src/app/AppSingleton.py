#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from src.app.extensions import db

app = Flask(__name__)
app.config.from_object('src.app.config')
db.init_app(app)
