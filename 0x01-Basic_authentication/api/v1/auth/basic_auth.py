#!/usr/bin/env python3
"""
Implementing Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns a decoded value of base64 string."""
        base64_header = base64_authorization_header
        if base64_header is not None and type(base64_header) == str:
            try:
                base64_bytes = base64_header.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                return message_bytes.decode('ascii')
            except Exception:
                pass
        return None
