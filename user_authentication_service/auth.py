#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password"""
    encoded_pwd = password.encode("utf-8")
    hashed = bcrypt.hashpw(encoded_pwd, bcrypt.gensalt())
    return hashed
