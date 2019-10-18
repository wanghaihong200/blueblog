#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: manage
@time: 2019/9/26 17:22
@desc:
"""
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from blog import create_app, db
from blueblog.models import Admin, Category, Post, Comment

app = create_app()
manager = Manager(app)

# 1. 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app=app, db=db)
# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()