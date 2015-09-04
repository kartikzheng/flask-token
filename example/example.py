# coding: utf-8

"""
    example
    ~~~~~~~

        使用 flask-token 扩展获取token的一个小例子
"""

from flask import Flask
from flask.ext.token import Token
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'it is hard to guss'
# app.config['SQLALCHEMY_DATABASE_URI'] = '/path/to/database'
app.config['SQLALCHEMY_DATABASE_URI'] = '/Users/www/project/flask_token/data.sqlite'


token = Token(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


from . import models, views, manage
