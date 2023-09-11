#!/usr/bin/python3
"""The City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city

    Attributes:
        state_id (str): State id
        name (str): City name
    """

    state_id = ""
    name = ""
