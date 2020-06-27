#!/usr/bin/python3
"""Defines a BaseModel class"""

import uuid
from datetime import datetime


class BaseModel:

    
    """Represents a BaseModel
    Attributes:
        id (string): generate an id for each BaseModel.
        created_at (integer): represent the current datetime when the instance is created.
        updated_at (integer): represent the current datetime when the instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if key is "created_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.created_at = value.isoformat()
            elif key is "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = value.isoformat()
            if key is not "__class__":
                setattr(self, key, value)

    def __str__(self):
        """returns an update for the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """returns an update for the updated_at"""
        self.updated_at = datetime.now()
        

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        model_dict = {}
        assign_dict(model_dict, self.__dict__)
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        model_dict["__class__"] = self.__class__.__name__
        return model_dict


def assign_dict(dest, src):
    """assign the value of src to dest"""
    for key, value in src.items():
        dest[key] = value
