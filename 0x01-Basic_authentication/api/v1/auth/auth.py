#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ hat returns False - path and object"""
        return False

    def authorization_header(self, request=None) -> str:
        """ that returns None - request will be the Flask request object"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return request
