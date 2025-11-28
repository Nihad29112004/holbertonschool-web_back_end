#!/usr/bin/env python3
"""Session authentication module.

This module contains the SessionAuth class that handles session-based
authentication for users.
"""

import uuid
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
from flask import request


class SessionAuth(Auth):
    """Session authentication class.

    Inherits from Auth. Handles creation and management of sessions
    in memory using a dictionary.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new Session ID for a given User ID.

        Args:
            user_id (str): The user ID to associate with the session.

        Returns:
            str: The session ID if successful, None otherwise.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieve a User ID based on a Session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The User ID linked to the session, or None if invalid.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar("User"):
        """Retrieve a User instance based on a Session ID from a request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            User: The User instance if session is valid, None otherwise.
        """
        if request is None:
            return None
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Delete a user session based on a Session ID cookie.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            bool: True if the session was successfully deleted,
                  False if request is None, cookie is missing, or session invalid.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if self.user_id_for_session_id(session_id) is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
