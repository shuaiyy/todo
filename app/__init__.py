#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : __init__.py
# @Author: Shuaiyy
# @Date  : 2017/9/22 20:32
# @Desc  : 
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

from app import models, views
if __name__ == '__main__':
    pass


