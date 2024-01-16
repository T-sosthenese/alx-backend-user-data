#!/usr/bin/env python3
"""
Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Implemetation of a class for autheticating users"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if path is not in excluded_paths"""
        if path is not None and excluded_paths is not None:
            if path[-1] != "/":
                path = path + "/"
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, requestNone) - str:
        """Validates all API requests for secure API"""
        if request is not None:
            dict_key = request.headers.get('Authorization')
            if dict_key is not None:
                return dict_key
        return None

    def current_user(self, requestNone) -> TypeVar('User'):
        """Returns the current user"""
        return None
