#!/usr/bin/env python3
"""Session Authentication view module."""
from flask import jsonify, request, abort, make_response
from models.user import User

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def login():
    """Handle user login using SessionAuth."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import auth instance here to avoid circular import
    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    cookie_name = auth.SESSION_NAME if hasattr(auth, 'SESSION_NAME') else "_my_session_id"

    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
