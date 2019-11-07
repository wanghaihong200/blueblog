#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2019/10/18 15:14
@desc:
"""
from flask import Blueprint

bp = Blueprint('api', __name__)

# 写在最后是为了防止循环导入， ping.py文件也会导入 bp
from app.api.ping import ping
from app.api import users
