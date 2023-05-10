#!/usr/bin/python3
"""
Defines the City class that inherits
from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city representation.

    Attributes:
        state_id (str): the state id of the city
        representation
        name (str): the represented city's name.
    """

    state_id=""
    name = ""
