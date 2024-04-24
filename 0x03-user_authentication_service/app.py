#!/usr/bin/env python3
"""main module"""
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root_():
    """root function"""
    jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
