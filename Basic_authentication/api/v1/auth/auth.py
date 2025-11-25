#!/usr/bin/env python3
"""
Authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class template for API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False for now, path and excluded_paths to be used later"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None for now, will return Authorization header later"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None for now, will return current authenticated user later"""
        return None
