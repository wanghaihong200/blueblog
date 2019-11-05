#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: app
@time: 2019/11/4 18:05
@desc:
"""
from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api_v2', __name__)
api = Api(bp)


#  统一注册路由
from app.api_v2 import urls
