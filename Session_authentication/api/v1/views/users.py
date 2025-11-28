#!/usr/bin/env python3
""" Users view module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a User object or the authenticated user if 'me'."""
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())
