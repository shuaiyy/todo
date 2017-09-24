#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : fabfile.py
# @Author: Shuaiyy
# @Date  : 2017/9/24 10:01
# @Desc  : 

from fabric.api import *

env.hosts = ['192.168.1.237']
env.user = 'sss'
env.password = 'sss'

def hello():
    print "hello!"

def deploy():
    with cd('/home/ubuntu/new/todo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')


