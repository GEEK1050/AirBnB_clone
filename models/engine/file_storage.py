#!/usr/bin/python3
"""Define a class FileStorage"""

import json
from datetime import datetime
from models.base_model import BaseModel

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
                my_dict[key] = value.to_dict()
            js_object = json.dumps(my_dict)
            my_file.write(js_object)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as my_file:
                dict_js = my_file.read()
                my_dict = json.loads(dict_js)
                for key, value in my_dict.items():
                    obj = eval(value["__class__"])
                    self.__objects[key] = obj(**value)
                    print("reload here")
                    self.__objects["{}.{}".format(self.__class__.__name__, obj.id)] = obj
        except:
            return
