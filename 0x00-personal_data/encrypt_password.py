#!/usr/bin/env python3
"""Encrypt password"""
import bcrypt
import typing


def hash_password(password: str) -> typing.ByteString:
    """hash password"""
    salt = bcrypt.gensalt()
    b_password = password.encode()
    hashed_pwd = bcrypt.hashpw(b_password, salt)
    return hashed_pwd
