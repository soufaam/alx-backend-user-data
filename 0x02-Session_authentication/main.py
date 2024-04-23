#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
<<<<<<< HEAD
    r = requests.get('http://0.0.0.0:5000/api/v1/users/me', cookies={'_my_session_id': "fake session ID"})
    if r.status_code != 403:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    print("OK", end="")
=======
    app.run(host="0.0.0.0", port="5000")
>>>>>>> parent of a638005... dix bug
