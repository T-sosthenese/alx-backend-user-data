#!/usr/bin/env python3
"""
Implements a has_password function to return a hashed password
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Compares the hased password and the unhashed pawword to see if they
    are the same.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
