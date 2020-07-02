#!/usr/bin/python3
"""Defines a BaseModel class"""

import uuid
from datetime import datetime
import models
import copy


class BaseModel:
    """Represents a BaseModel
    Attributes:
        id (string): generate an id for each BaseModel.
        created_at (integer): represent the current
        datetime when the instance is created.
        updated_at (integer): represent the current
        datetime when the instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value,
                                              "%Y-%m-%dT%H:%M:%S.%f")
                    print(type(value))
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns an update for the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """returns an update for the updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        model_dict = {}

        model_dict = copy.deepcopy(self.__dict__)
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        model_dict["__class__"] = self.__class__.__name__
        return model_dict


def assign_dict(dest, src):
    """assign the value of src to dest"""
    for key, value in src.items():
        if key != 'created_at' and key != "updated_at":
            dest[key] = value
