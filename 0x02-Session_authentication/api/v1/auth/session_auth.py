#!/usr/bin/env python3
"""Module: session authentication"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    A class showing implementation of session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session_id based on a given user_id"""
        if user_id is not None and type(user_id) == str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user id based on a session id"""
        if session_id is not None and type(session_id) == str:
            user_id = self.user_id_by_session_id.get(session_id)
            if user_id is not None:
                return user_id
            return None

    def current_user(self, request=None):
        """Returns a User instance based on cookie value"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes a user session"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
