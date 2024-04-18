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
