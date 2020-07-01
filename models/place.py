#!/usr/bin/python3
"""Defines the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place class.
    Attributes:
        city_id (str): id of City.
        user_id (str): id of User.
        name (str): name of the place.
        description (str): place description.
        number_rooms (int): The number of rooms in place.
        number_bathrooms (int): The number of bathrooms in place.
        max_guest (int): The maximum number of guests in place.
        price_by_night (int): The price by night in place.
        latitude (float): The latitude in place.
        longitude (float): The longitude in place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
