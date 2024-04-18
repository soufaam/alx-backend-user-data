#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
from .auth import Auth


class BasicAuth(Auth):
    """BasicAuth that inherits from Auth.
    For the moment this class will be empty.
    """
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """class BasicAuth that returns the Base64 part of
        the Authorization header for a Basic Authentication:"""
        if not authorization_header or\
                not isinstance(authorization_header, str)\
                or not authorization_header.startswith('Basic '):
            return None
        result = authorization_header.replace('Basic ', '')
        return result
