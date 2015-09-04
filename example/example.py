# coding: utf-8

"""
    example
    ~~~~~~~

        使用 flask-token 扩展获取token的一个小例子
"""

from flask import Flask, g, jsonify
from flask.ext.token import Token, TokenBase
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'it is hard to guss'
app.config['SQLALCHEMY_DATABASE_URI'] = '/path/to/database'


token = Token(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


class User(db.Model, UserMixin, TokenBase):
    """用户类"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(164))
    password_hash = db.Column(db.String(164))

    @login_manager.user_loader
    def load_user(user_id):
        """flask-login要求实现的用户加载回调函数
           依据用户的unicode字符串的id加载用户"""
        return User.query.get(int(user_id))

    @property
    def password(self):
        """将密码方法设为User类的属性"""
        raise AttributeError('无法读取密码原始值!')

    @password.setter
    def password(self, password):
        """设置密码散列值"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """验证密码散列值"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "%r :The instance of class User" % self.username


@token.verify_password
def verify_password(username_or_token, password):
    user = User.verify_token(username_or_token)
    if not user:
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/api/token')
@token.login_required
def get_token():
    token = g.user.generate_token(3600)
    return jsonify({'token':token.decode('ascii')})


if __name__ == '__main__':
    app.run(debug=True)
