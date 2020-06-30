#!/usr/bin/python3
"""Define a class FileStorage"""

import json
import os
from datetime import datetime
from models.base_model import BaseModel
import copy


class FileStorage:
    """serialize instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set in __objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as my_file:
            my_dict = {}
            for key, value in self.__objects.items():
                tmp = copy.deepcopy(value)
                my_dict[key] = tmp.to_dict()
            js_object = json.dumps(my_dict)
            my_file.write(js_object)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if (os.path.exists(self.__file_path)
           and os.path.getsize(self.__file_path)):
            try:
                with open(self.__file_path, "r") as my_file:
                    my_dict = json.loads(my_file.read())
                    for key, value in my_dict.items():
                        obj = eval(value["__class__"])(**value)
                        self.__objects[key] = obj
            except FileNotFoundError:
                return
