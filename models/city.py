#!/usr/bin/python3
"""Defines the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city class.
    Attributes:
        state_id (str): id state.
        name (str): city name.
    """

    state_id = ""
    name = ""
