#!/usr/bin/env python3
"""Users view module for API.
Defines routes for user operations.
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a User object.
    Args:
        user_id (str): ID of the user to retrieve. Can be "me".
    Returns:
        JSON representation of the user.
    """
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())

    user = User.get(user_id)
    if user is None:
        abort(404)

    return jsonify(user.to_json())
