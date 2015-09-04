#!/usr/bin/env python
# encoding: utf-8

"""flask-token: 快速生成API认证令牌"""

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request
from flask.ext.httpauth import HTTPBasicAuth, HTTPDigestAuth
from functools import wraps


class Token(HTTPBasicAuth, HTTPDigestAuth):

    def __init__(self, app=None):
        super(Token, self).__init__()
        self.app = app
        if app is not None:
            self.init_app(app)

        def default_get_password(username):
            return None

        def default_auth_error():
            return '禁止访问,我是大魔王,哈哈哈哈哈哈哈'

        self.realm = "Authentication Required"
        self.get_password(default_get_password)

    def init_app(self, app):
        pass

    def get_password(self, f):
        self.get_password_callback = f
        return f

    def login_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if request.method != 'OPTIONS':
                if auth:
                    password = self.get_password_callback(auth.username)
                else:
                    password = None
                if not self.authenticate(auth, password):
                    return self.auth_error_callback()
            return f(*args, **kwargs)
        return decorated


class TokenBase(object):
    """生成令牌，验证令牌"""

    def generate_token(self, expiration):
        s = Serializer(
            current_app.config['SECRET_KEY'],
            expires_in=expiration
        )
        return s.dumps({'id': self.id}).decode('ascii')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return "the instance of class TokenBase"
