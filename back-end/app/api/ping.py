#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: ping
@time: 2019/10/18 15:28
@desc:
"""
from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    """
    前端vue用来测试 与 后端 flask api 的连通性
    :return:
    """
    return jsonify('Connect successful!')
