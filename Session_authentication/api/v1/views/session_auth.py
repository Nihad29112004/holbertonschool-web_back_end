#!/usr/bin/env python3
"""Session authentication views"""
from flask import request, jsonify, make_response, abort
from api.v1.views import app_views
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Login route for session authentication"""
    from api.v1.app import auth
    if auth is None:
        abort(404)

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email.strip() == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password.strip() == "":
        return jsonify({"error": "password missing"}), 400

    from models.user import User
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    res = make_response(jsonify(user.to_json()))
    cookie_name = getenv("SESSION_NAME")
    if cookie_name:
        res.set_cookie(cookie_name, session_id)
    return res
