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
elif AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """404 error"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """401 error"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """403 error"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """Assign current_user and check authentication"""
    if auth is None:
        request.current_user = None
        return

    request.current_user = auth.current_user(request)

    excluded_paths = [
        "/api/v1/status",
        "/api/v1/status/",
        "/api/v1/unauthorized",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden",
        "/api/v1/forbidden/",
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if request.current_user is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
