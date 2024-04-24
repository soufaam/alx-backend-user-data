#!/usr/bin/env python3
"""authentication module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """return bytes is a salted hash"""
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password_byte, salt)
    return hash_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=hashed)
            return new_user