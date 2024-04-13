#!/usr/bin/env python3
"""Encrypt password"""
import bcrypt
import typing


def hash_password(password: str) -> bytes:
    """hash password"""
    salt = bcrypt.gensalt()
    b_password = password.encode("utf-8")
    hashed_pwd = bcrypt.hashpw(b_password, salt)
    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """function that expects 2 arguments """
    return bcrypt.checkpw(password, hashed_password)
