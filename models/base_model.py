#!/usr/bin/python3
"""
This is the parent class from which other
classes' properties will inherit.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        updates attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
        returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        return class_name + " (" + self.id + ") " + self.__dict__
