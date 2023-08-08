#!/usr/bin/env python3
"""
BasicAuth class to manage the API authentication.
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class to manage the API authentication.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Public method to return the Base64 part of the
        Authorization header for a Basic Authentication.
        """
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Public method to return the decoded value of a Base64 string.
        """
        if base64_authorization_header is None or\
                type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
