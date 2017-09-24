#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : manage.py
# @Author: Shuaiyy
# @Date  : 2017/9/22 20:32
# @Desc  : 
from flask_script import Manager
from app import app
from app.models import Todo

manage = Manager(app)


@manage.command
def save():
    t = Todo(content='写作业')
    t.save()

@manage.command
def list():
    t = Todo.objects.all()
    for x in t:
        print x
        # for i in x:
        #     print i, x[i]

if __name__ == '__main__':
    manage.run()


