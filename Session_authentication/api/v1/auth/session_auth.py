#!/usr/bin/env python3
"""Session authentication module."""

import uuid
from typing import TypeVar
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session authentication class.

    Inherits from Auth.
    Manages sessions with in-memory storage.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a given user_id.

        Args:
            user_id (str): The user ID.

        Returns:
            str or None: The session ID, or None if user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return a User ID based on a Session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str or None: The user ID if session exists, None otherwise.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None for all requests.
        Minimal implementation for now.
        """
        return None
