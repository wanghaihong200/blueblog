# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
toolbar = DebugToolbarExtension()
migrate = Migrate()
