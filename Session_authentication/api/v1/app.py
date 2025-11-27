#!/usr/bin/env python3
""" API app """
from os import getenv
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.views import app_views

auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """ Run before each request """
    if auth is None:
        return

    # Excluded paths
    excluded_paths = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/",
    ]

    # Require authentication?
    if auth.require_auth(request.path, excluded_paths):

        # Missing Authorization header → 401
        if auth.authorization_header(request) is None:
            abort(401)

        # Resolve user
        if auth.current_user(request) is None:
            abort(403)

        # 🔥 Holberton’un istediği adım
        request.current_user = auth.current_user(request)

    else:
        # Excluded endpointlerde current_user None olsun
        request.current_user = None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
