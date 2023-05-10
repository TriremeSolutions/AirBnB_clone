#!/usr/bin/python3
"""
Defines the Place class that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a place representation.

    Attributes:
        city_id (str): the city id of the place
        representation
        user_id (str): the user id.
        name (str): the place's name.
        description (str): The place's description.
        number_rooms (int): The place's room count.
        number_bathrooms (int): The place's bathroom count.
        max_guest (int): The places's max guests intake.
        price_by_night (int): The place's price per night.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
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
