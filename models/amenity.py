#!/usr/bin/python3
"""The Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of an amenity

    Attributes:
        name (str): Amenity name
    """

    name = ""
