#!/usr/bin/env python3
"""
User model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Represents a system user with authentication attributes.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
