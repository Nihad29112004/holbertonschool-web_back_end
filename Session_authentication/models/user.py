#!/usr/bin/env python3
"""
User model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Represents a system user for authentication.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
