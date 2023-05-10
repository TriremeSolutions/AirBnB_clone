#!/usr/bin/python3
"""
Defines the Amenity class that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an amenity representation.

    Attributes:
        name (str): the represented amenity's name.
    """

    name = ""
