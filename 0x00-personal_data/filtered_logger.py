#!/usr/bin/env python3
"""
A module used for obfuscation of user data.
"""
from typing import List
import re
import logging
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns an obfuscated log message
    Args:
        fields (list): A list of strings showing fields for obfuscation
        redaction (str): What the field will be obfuscated to
        message (str): the log line to be obfuscated
        separator (str): the character separating the fields
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
