#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : models.py
# @Author: Shuaiyy
# @Date  : 2017/9/22 20:31
# @Desc  : 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField(required=True, max_length=30)
    time = db.DateTimeField(default=datetime.datetime.now)
    status = db.IntField(default=0)

    def __str__(self):
        return "content:{} time:{} status:{}".format(self.content, self.time, self.status)

TodoFrom = model_form(Todo)

if __name__ == '__main__':
    pass


