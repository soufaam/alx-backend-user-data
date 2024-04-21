#!/usr/bin/python3
""" Check response
"""
import requests

if __name__ == "__main__":
    r = requests.get('http://0.0.0.0:5000/api/v1/auth_session/login')
    if r.status_code != 404 and r.status_code != 405:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    print("OK", end="")
