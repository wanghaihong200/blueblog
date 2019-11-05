#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: ping
@time: 2019/11/4 17:42
@desc:
"""
from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return {
            'message': "Connect Successful!"
        }
