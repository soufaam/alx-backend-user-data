#!/usr/bin/env python3
"""authentication module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Optional, TypeVar


UserT = TypeVar("UserT", bound=User)


def _hash_password(password: str) -> bytes:
    """return bytes is a salted hash"""
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password_byte, salt)
    return hash_pwd


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    value = uuid.uuid4().__str__()
    return value


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user add it to DB"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=hashed)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login"""
        try:
            found_user = self._db.find_user_by(email=email)
        except Exception:
            return False
        fpassword = found_user.hashed_password
        return bcrypt.checkpw(password.encode("utf-8"), fpassword)

    def create_session(self, email: str):
        """returns the session ID as a string"""
        try:
            found_user = self._db.find_user_by(email=email)
        except Exception:
            return None
        session_id = _generate_uuid()
        self._db.update_user(found_user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> UserT:
        """eturns the corresponding User or None"""
        if not session_id:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destry session"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            pass
        return None

    def get_reset_password_token(self, email: str) -> Optional[str]:
        """Reset password token"""
        try:
            new_user = self._db.find_user_by(email=email)
            reset_token = str(uuid.uuid4())
            self._db.update_user(new_user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """update the user’s hashed_password"""
        if reset_token is None or password is None:
            raise ValueError
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except Exception:
            raise ValueError
        hpassword = _hash_password(password=password)
        self._db.update_user(user.id,
                             hashed_password=hpassword, reset_token=None)
