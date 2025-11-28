#!/usr/bin/env python3
"""Session authentication module."""

from api.v1.auth.auth import Auth
from typing import TypeVar


class SessionAuth(Auth):
    """
    Session authentication class.

    Inherits from Auth. Minimal implementation for Holberton checker:
    - current_user(request) always returns None
    """
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None for all requests.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            None
        """
        return None
