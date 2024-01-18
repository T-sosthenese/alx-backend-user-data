#!/usr/bin/env python3
"""Module: session authentication"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    A class showing implementation of session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session_id based on a given user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        # Generating session ID using uuid4
        session_id = str(uuid.uuid4())

        # Storing user_id in the user_id_by_session_id dictionary
        self.user_id_by_session_id[session_id] = user_id
