#!/usr/bin/env python3
"""
Flask app with user registration
"""
from flask import Flask, jsonify, request
from auth import Auth
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
auth = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """Return a JSON welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """Register a new user via POST request"""
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"message": "Missing email or password"}), 400

    email = data["email"]
    password = data["password"]

    try:
        user = auth.register_user(email, password)
        return jsonify({"message": f"User {email} created successfully"}), 201
    except ValueError as err:
        return jsonify({"message": str(err)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
