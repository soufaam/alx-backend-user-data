#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
from .auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        Args:
            base64_authorization_header (str): _description_
        Returns:
            str: _description_
        """
        if not base64_authorization_header or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            value = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return value
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """returns the user email and password from the Base64 decoded value.
        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        if not decoded_base64_authorization_header or\
                not isinstance(decoded_base64_authorization_header, str)\
                or ":" not in decoded_base64_authorization_header:
            return (None, None)
        mail, password = tuple(decoded_base64_authorization_header.split(":"))
        return mail, password
