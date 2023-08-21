#!/usr/bin/python3
"""
Defines a class Amenity.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
