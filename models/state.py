#!/usr/bin/python3
"""
Defines the State class that inherits
from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a state representation.

    Attributes:
        name (str): the represented state's name.
    """

    name = ""
