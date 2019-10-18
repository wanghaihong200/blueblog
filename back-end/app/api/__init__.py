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

# 在文件最后导入，是为了防止循环导入
from app.api.ping import ping
