#!/usr/bin/env python3
"""Status endpoint"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return API status"""
    return jsonify({"status": "OK"})
