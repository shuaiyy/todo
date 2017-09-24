#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : views.py
# @Author: Shuaiyy
# @Date  : 2017/9/22 20:31
# @Desc  : 
from app import app
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template, request
from app import app
from models import Todo, TodoFrom

@app.route('/')
def index():
    form = TodoFrom()
    todos = Todo.objects.all()
    return render_template('index.html', **locals())

@app.route('/add', methods=['POST'])
def add():
    form = TodoFrom(request.form)
    if form.validate():
        todo = Todo(content=form.content.data)
        todo.save()
    else:
        print form.errors
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', **locals())

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoFrom()
    todo = Todo.objects(id=todo_id)
    if todo:
        todo.update(status=1)
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', **locals())

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoFrom()
    todo = Todo.objects.get_or_404(id=todo_id)
    if todo:
        todo.update(status=0)
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', **locals())

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoFrom()
    todo = Todo.objects.get_or_404(id=todo_id)
    if todo:
        todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', **locals())

if __name__ == '__main__':
    pass


