#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2019/10/9 17:55
@desc:
"""
from flask import Flask
from app.api import bp
from settings import config
import os
from extensions import bootstrap, db, migrate, moment, ckeditor, mail
# from blueblog.models import Admin, Category
import click


def register_extensions(app):
    # 加载第三方扩展
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)


def register_logging(app):
    # 日志
    pass


def register_blueprints(app):
    # 注册路由
    app.register_blueprint(bp, url_prefix='/api')
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    # app.register_blueprint(blog_bp, url_prefix='/blog')


def register_shell_context(app):
    # 注册shell上下文出来函数
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    # 注册模板上下文处理函数
    # @app.context_processor
    # def make_template_context():
    #     admin = Admin.query.first()
    #     categories = Category.query.order_by(Category.name).all()
    #     return dict(admin=admin, categories=categories)
    pass


def register_errors(app):
    # 注册错误处理函数
    # @app.errorhandler(400)
    # def bad_request(e):
    #     return render_template('errors/400.html'), 400
    pass


def register_commands(app):
    # 注册自定义shell命令
    @app.cli.command()
    @click.option('--category', default=10)
    @click.option('--post', default=50)
    @click.option('--comment', default=500)
    def forge(category, post, comment):
        # from blueblog.fakes import fake_admin, fake_categories, fake_posts, fake_comments
        #
        # click.echo('开始生成admin表数据。。。。')
        # fake_admin()
        #
        # click.echo('开始生成 %d 条category表数据。。。。' % category)
        # fake_categories(category)
        #
        # click.echo('开始生成 %d 条post表数据。。。。' % post)
        # fake_posts(post)
        #
        # click.echo('开始生成 %d 条comments表数据。。。。' % comment)
        # fake_comments(comment)
        #
        # click.echo('Done.')
        pass


# app工厂函数
def create_app(config_name=None, template_folder='templates'):
    # 配置环境变量
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])

    register_extensions(app)  # 第三方扩展初始化
    register_logging(app)  # 日志处理器
    register_blueprints(app)  # 注册蓝本路由
    register_shell_context(app)  # 注册shell上下文出来函数
    register_template_context(app)  # 注册模板上下文处理函数
    register_errors(app)  # 注册错误处理函数
    register_commands(app)  # 注册自定义shell命令

    return app
