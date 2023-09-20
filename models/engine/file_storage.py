#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Dictionary to map class names to their respective classes
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""

    def __init__(self):
        """Initialize FileStorage instance."""
        self.__file_path = "file.json"
        self.__objects = {}  # Dictionary to store all objects by class_name.id

    def all(self, cls=None):
        """Returns the dictionary of all objects or of a specific class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for key, value in jo.items():
                cls_name = value["__class__"]
                self.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Call reload() method to deserialize the JSON file to objects."""
        self.reload()
