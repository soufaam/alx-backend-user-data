#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ hat returns False - path and object"""
        if path and path[-1] != '/':
            path = path + '/'
        if not path or not excluded_paths or path not in excluded_paths:
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

    def session_cookie(self, request=None):
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        print("here session1")
        cookie_name = request.cookies.get(session_name, None)
        print("here cookie")
        return cookie_name
