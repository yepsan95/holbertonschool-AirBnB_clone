#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Represents the base model for the AirBnB clone project.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.
        """

        self.updated_at = datetime.today()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__
        of the instance.
        """

        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__

        return r_dict

    def __str__(self):
        """
        Returns the string representation of hte object.
        """

        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
