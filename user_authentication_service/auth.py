#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password"""
    encoded_pwd = password.encode("utf-8")
    hashed = bcrypt.hashpw(encoded_pwd, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password"""
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            # If no exception → user exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # User does not exist, proceed to create
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user
