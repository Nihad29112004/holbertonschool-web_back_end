#!/usr/bin/env python3
""" Basic Auth class """
import base64
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from models.user import User

class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if type(authorization_header) is not str or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded: str) -> Tuple[str, str]:
        if type(decoded) is not str or ":" not in decoded:
            return None, None
        return tuple(decoded.split(":", 1))

    def user_object_from_credentials(self, email: str, pwd: str) -> TypeVar('User'):
        if type(email) is not str or type(pwd) is not str:
            return None
        users = User.search({"email": email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64)
        email, pwd = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, pwd)
