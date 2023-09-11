#!/usr/bin/python3
"""The Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of a place

    Attributes:
        city_id (str): City id
        user_id (str): User id
        name (str): Place  name
        description (str):  Place description
        number_rooms (int): Number of rooms of the place
        number_bathrooms (int): Number of bathrooms of the place
        max_guest (int): Guests maximum number of the place
        price_by_night (int): Price by night of the place
        latitude (float):  Place latitude
        longitude (float): Place longitude
        amenity_ids (list): Amenity list ids
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
