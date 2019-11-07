#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: users
@time: 2019/11/5 14:05
@desc:
"""
from flask_restful import Resource, reqparse, inputs
from flask import url_for
from app.models import User
from extensions import db


# 针对单个用户的注册，删除，查询
class UserAPI(Resource):
    def __init__(self):
        pass

    def get(self, id):
        pass

    def delete(self, id):
        pass

    def put(self, id):
        pass


# 一堆用户的查询，注册
class UserListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('username', type=str, required=True, help='请输入一个正确的username', location='json')
        self.parser.add_argument('email', type=inputs.regex('\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}'), required=True, help='请输入一个正确的email', location='json', trim=True)
        self.parser.add_argument('password', type=str, required=True, help='请输入一个正确的密码', location='json')
        super(UserListAPI, self).__init__()

    def get(self):
        pass

    def post(self):
        """ 注册新用户 """
        args = self.parser.parse_args(strict=True)

        # 如果用户名或邮箱地址已被占用， 返回错误提示
        message = {}
        if User.query.filter_by(username=args.get('username', None)).first():
            message['username'] = '用户名已存在！'
        if User.query.filter_by(email=args.get('email', None)).first():
            message['email'] = '邮箱已存在！'
        if message:
            return {'message': message}, 400

        # 写入数据库
        user = User()
        user.from_dict(args, new_user=True)
        db.session.add(user)
        db.session.commit()

        # 返回新增的用户数据
        return user.to_dict(), 201, {'Location': url_for('api_v2.user', id=user.id)}
