#!/usr/bin/env python3
"""
Main file
"""
import requests
import uuid


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Register user"""
    url = "http://127.0.0.1:5000/users"
    response = requests.post(url=url, data={
        "email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {
        "email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Wrong Login user"""
    url = "http://127.0.0.1:5000/sessions"
    response = requests.post(url=url, data={
        "email": email, "password": password})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Log in """
    url = "http://127.0.0.1:5000/sessions"
    response = requests.post(url=url, data={
        "email": email, "password": password})
    session_id = response.cookies.get("session_id")
    assert response.status_code == 200
    assert response.json() == {
        "email": email, "message": "logged in"}
    return session_id


def profile_unlogged() -> None:
    """Log out"""
    cookies = {'session_id': f'{uuid.uuid4().__str__()}'}
    url = "http://127.0.0.1:5000/profile"
    response = requests.get(url=url, cookies=cookies)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """profile logged"""
    cookies = {'session_id': session_id}
    url = "http://127.0.0.1:5000/profile"
    response = requests.get(url=url, cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """log out func"""
    url = "http://127.0.0.1:5000/sessions"
    response = requests.delete(url=url, cookies={"session_id": session_id})
    assert response.json() == {'message': 'Bienvenue'}
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """reset password token"""
    url = "http://127.0.0.1:5000/reset_password"
    response = requests.post(url=url, data={"email": email})
    reset_token = response.json().get("reset_token")
    assert response.status_code == 200
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """password update"""
    url = "http://127.0.0.1:5000/reset_password"
    response = requests.put(url=url, data={
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
