#!/usr/bin/env python3
"""
Basic authentication module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication class that inherits from Auth """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Split into two parts: "Basic" and the Base64 string
        return authorization_header.split(" ", 1)[1]
