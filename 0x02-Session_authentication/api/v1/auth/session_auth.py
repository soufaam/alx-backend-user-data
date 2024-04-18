#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
from .auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """
    Class SessionAuth
        Args:
        Auth (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
