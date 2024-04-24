#!/usr/bin/env python3
"""main module"""
from flask import Flask
from flask import jsonify
from auth import Auth
from flask import request


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root_():
    """root function"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """ function that implements the POST /users"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": f"{user.email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
