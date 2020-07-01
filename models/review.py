#!/usr/bin/python3
"""Defines the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review class.
    Attributes:
        place_id (str): id place.
        user_id (str): id user.
        text (str): review text.
    """

    place_id = ""
    user_id = ""
    text = ""
