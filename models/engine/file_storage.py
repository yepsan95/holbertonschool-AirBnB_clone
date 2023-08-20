#!/usr/bin/python3
"""
Defines class FileStorage.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and viceversa.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Stores all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """

        object_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[object_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """

        dict = FileStorage.__objects
        obj_dict = {obj: dict[obj].to_dict() for obj in dict.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the SON file to __objects
        (only if the JSON file (__file_path) exists).
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
