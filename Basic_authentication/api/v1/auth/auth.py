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

        # Ensure path ends with a slash for comparison
        if not path.endswith("/"):
            path += "/"

        for excluded in excluded_paths:
            if excluded.endswith("/"):
                if path == excluded:
                    return False
            else:
                if path.rstrip("/") == excluded:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None for now. request is the Flask request object
        """
        return None

    def current_user(self, request=None):
        """
        Returns None for now. request is the Flask request object
        """
        return None
