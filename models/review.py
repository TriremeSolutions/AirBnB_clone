#!/usr/bin/python3
"""
Defines the Review class that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a user review representation.

    Attributes:
        place_id (str): the place id of the review
        representation
        user_id (str): the user id.
        text: the review text body
    """

    place_id = ""
    user_id = ""
    text = ""
