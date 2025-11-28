#!/usr/bin/env python3
"""Session Authentication Views."""
from flask import request, jsonify, abort, make_response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handle POST /auth_session/login to create a session for a user."""
    # Import here to avoid circular import
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email.strip() == "":
        return jsonify({"error": "email missing"}), 400

    if password is None or password.strip() == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    if session_id is None:
        abort(500)

    resp = make_response(jsonify(user.to_json()))
    cookie_name = os.getenv("SESSION_NAME")
    resp.set_cookie(cookie_name, session_id)
    return resp
