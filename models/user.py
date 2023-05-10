#!/usr/bin/python3
"""
User class that inherits from
BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines creation of new user
    Attributes:
        email (str): user email.
        password (str): user password.
        first_name (str): user's first name.
        last_name (str): user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
