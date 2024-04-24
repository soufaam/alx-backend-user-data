#!/usr/bin/env python3
"""authentication module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """return bytes is a salted hash"""
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password_byte, salt)
    return hash_pwd
