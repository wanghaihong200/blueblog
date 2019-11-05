#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: settings
@time: 2019/10/10 16:50
@desc:
"""
import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))  # 项目的根目录  "blog/back-end"
load_dotenv(os.path.join(basedir, '.flaskenv'))  # 载入环境配置文件
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(basedir)


class BaseConfig(object):
    SECRET_KEY = b'\x07\x83\x17!\xd3Ll\xdf$i\xd6\xa7L\xca\xb9\xad'  # 密匙
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # orm 操作追踪

    # 邮件配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'xxx')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'xxx')
    MAIL_DEFAULT_SENDER = ('海海', MAIL_USERNAME)

    BLUELOG_EMAIL = 'AAA'
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    USERNAME = os.getenv('USER', 'xxx')  # 用户名
    PASSWORD = os.getenv('PASSWORD', 'xxx')  # 密码
    HOST = os.getenv('HOST', '127.0.0.1')  # 数据库地址
    PORT = os.getenv('PORT', '3306')  # 端口
    DATABASE = os.getenv('DATABASE', 'xxx')  # 数据库名
    database_url = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    USERNAME = os.getenv('USER', 'xxx')  # 用户名
    PASSWORD = os.getenv('PASSWORD', 'xxx')  # 密码
    HOST = os.getenv('HOST', '127.0.0.1')  # 数据库地址
    PORT = os.getenv('PORT', '3306')  # 端口
    DATABASE = os.getenv('DATABASE', 'xxx')  # 数据库名
    database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = database_url
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    USERNAME = os.getenv('USER', 'xxx')  # 用户名
    PASSWORD = os.getenv('PASSWORD', 'xxx')  # 密码
    HOST = os.getenv('HOST', '127.0.0.1')  # 数据库地址
    PORT = os.getenv('PORT', '3306')  # 端口
    DATABASE = os.getenv('DATABASE', 'xxx')  # 数据库名
    database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
# 1
