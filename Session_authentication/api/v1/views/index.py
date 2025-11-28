#!/usr/bin/env python3
"""Index / status route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return OK status"""
    return jsonify({"status": "OK"})
