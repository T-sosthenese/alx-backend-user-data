#!/usr/bin/env python3
"""
Implementing Basic Authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class for basic authentications"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts basic auth password from header"""
        auth_header = authorization_header
        if auth_header is not None and type(auth_header) == str:
            if auth_header.startswith("Basic "):
                return auth_header[6:]
        return None
