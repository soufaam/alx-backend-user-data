#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ hat returns False - path and object"""
        if path and path[-1] != '/':
            path = path + '/'
        if not excluded_paths or not path:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*"):
                excluded_path.replace("*", ".*")
            if not bool(re.search(excluded_path, path)):
                return True
        return False

    def authorization_header(self, request=None) -> str:
        """ that returns None - request will be the Flask request object"""
        if not request:
            return None
        result = request.headers.get('Authorization', None)
        return result

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return None
