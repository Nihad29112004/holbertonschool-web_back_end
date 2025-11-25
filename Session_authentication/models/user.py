#!/usr/bin/env python3
""" User model """
import uuid

class User:
    __users = []

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.email = ""
        self.password = ""
        self.first_name = None
        self.last_name = None

    def save(self):
        User.__users.append(self)

    @classmethod
    def all(cls):
        return cls.__users

    @classmethod
    def get(cls, user_id):
        for u in cls.__users:
            if u.id == user_id:
                return u
        return None

    @classmethod
    def search(cls, query):
        results = []
        for u in cls.__users:
            match = True
            for k, v in query.items():
                if getattr(u, k, None) != v:
                    match = False
            if match:
                results.append(u)
        return results

    def is_valid_password(self, pwd):
        return self.password == pwd

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
