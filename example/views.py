# coding: utf-8

from . import app, token
from flask import g, jsonify


@app.route('/api/token')
@token.login_required
def get_token():
    token = g.user.generate_token(3600)
    return jsonify({"token":token.decode('ascii')})
