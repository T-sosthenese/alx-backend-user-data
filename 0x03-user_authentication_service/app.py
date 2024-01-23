#!/usr/bin/env python3
"""
A simple flask application with user authentication functionalities
"""
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Returns payload's homepage
    """
    return jsonify({"message": "Bienvenue"})
