#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: users
@time: 2019/11/5 14:05
@desc:
"""
from flask_restful import Resource


# 针对单个用户的注册，删除，查询
class UserAPI(Resource):
    def get(self, id):
        pass

    def delete(self, id):
        pass

    def put(self, id):
        pass


# 一堆用户的查询，注册
class UserListAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass
