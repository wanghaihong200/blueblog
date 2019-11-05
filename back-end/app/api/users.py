#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: users
@time: 2019/11/1 15:16
@desc:
"""
from app.api import bp
import re
from flask import request, jsonify, url_for
from app import db
from app.api.errors import bad_request
from app.models import User


@bp.route('/users', methods=['POST'])
def create_user():
    '''新用户注册'''
    data = request.get_json()


@bp.route('/users', methods=['GET'])
def get_users():
    '''查询多个用户，返回集合'''
    pass


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    '''返回单个用户'''
    pass


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    '''修改一个用户'''
    pass


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    '''删除一个用户'''
    pass
