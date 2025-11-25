#!/usr/bin/env python3
""" Initialize blueprint for API v1 """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
