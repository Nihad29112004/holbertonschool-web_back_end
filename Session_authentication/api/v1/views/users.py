#!/usr/bin/env python3
""" Users routes """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    users = [u.to_json() for u in User.all()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id=None):
    if user_id == "me":
        if getattr(request, "current_user", None) is None:
            abort(404)
        return jsonify(request.current_user.to_json())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())
