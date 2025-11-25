#!/usr/bin/env python3
"""
Authentication module
"""

from typing import List
from flask import request


class Auth:
    """
    Auth class template for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication.

        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths (slash-tolerant)
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded in excluded_paths:
            if excluded.endswith("/"):
                if path == excluded:
                    return False
            else:
                if path.rstrip("/") == excluded.rstrip("/"):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Return value of Authorization header in request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None):
        """
        Returns None for now. request is the Flask request object
        """
        return None
