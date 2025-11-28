#!/usr/bin/env python3
"""Auth module for Holberton School."""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Base authentication class.

    Methods to be inherited by other authentication mechanisms:

    - require_auth(path, excluded_paths): Check if authentication is required
      for a given path.
    - authorization_header(request): Return the Authorization header from a request.
    - current_user(request): Return the current user (None by default).
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if the requested path requires authentication.

        Args:
            path (str): The request path.
            excluded_paths (List[str]): List of paths that do not require auth.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or not excluded_paths:
            return True
        if path.endswith('/'):
            path = path
        else:
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Return the Authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str or None: The Authorization header, or None if not present.
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return the current user.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            None: Always returns None in the base class.
        """
        return None
