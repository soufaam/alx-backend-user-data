#!/usr/bin/env python3
"""main module"""
from flask import Flask
from flask import jsonify
from auth import Auth
from flask import request, abort, redirect


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


@app.route('/sessions', methods=['POST'])
def login():
    """login function"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email=email, password=password):
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", AUTH.create_session(email))
        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """logout"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)


@app.route("/profile", methods=['GET'])
def profile():
    """profile"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
