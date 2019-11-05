#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: urls
@time: 2019/11/4 17:51
@desc:
"""
from app.api_v2.app import api
from app.api_v2.resources.ping import Ping

# 统一注册路由
api.add_resource(Ping, '/', '/ping')
