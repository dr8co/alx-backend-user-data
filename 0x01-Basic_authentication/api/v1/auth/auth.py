#!/usr/bin/env python3
"""
Class to manage the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to require authentication for all routes
        except for excluded_paths.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:-1]):
                    return False
            elif path == p:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method to validate if an authorization header is present
        and contains the Base64 encoded value of the API key.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method to overloads current_user - and
        returns None for now.
        """
        return None
