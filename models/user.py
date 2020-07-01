#!/usr/bin/python3
"""Defines the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Initiation User class

    Attributes:
        email (str): user email.
        password (str): password of the user.
        first_name (str): user first name of.
        last_name (str): user last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
