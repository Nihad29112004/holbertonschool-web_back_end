#!/usr/bin/env python3
""" Auth class """
from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or not excluded_paths:
            return True
        if path.endswith('/'):
            path = path
        else:
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        return None
