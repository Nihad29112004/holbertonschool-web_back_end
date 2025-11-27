#!/usr/bin/env python3
""" Users views """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ GET /api/v1/users/<user_id> """

    # 🔥 Eğer URL: /api/v1/users/me ise
    if user_id == "me":
        # Kullanıcı doğrulanmamışsa → 404
        if request.current_user is None:
            abort(404)
        # Doğrulanmışsa kendi profilini döndür
        return jsonify(request.current_user.to_json())

    # Normal user id ile arama
    user = User.get(user_id)
    if user is None:
        abort(404)

    return jsonify(user.to_json())
