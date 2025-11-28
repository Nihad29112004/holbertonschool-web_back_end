#!/usr/bin/env python3
"""Session authentication module."""

import uuid
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Session authentication class.

    Inherits from Auth.
    Manages sessions with in-memory storage.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a given user_id."""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None) -> str:
        """Return the cookie value from request, if exists."""
        if request is None:
            return None
        cookie_name = getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(cookie_name)

    def current_user(self, request=None) -> TypeVar('User'):
        """Return a User instance based on session cookie."""
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
