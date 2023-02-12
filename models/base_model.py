#!/usr/bin/python3
"""This class model defines all methods for other classes"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines Attributes required by the base Model"""
    def __init__(self, *args, **kwargs):
        """Handles initialization of the base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                            kwargs["created_at"], "%Y-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value

        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the base model"""

        return ("[{}] ({}) {}".
                format(self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """Updates the attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the keys/values of the instance"""

        x_dict = self.__dict__.copy()
        x_dict["created_at"] = self.created_at.isformat()
        x_dict["updated_at"] = self.updated_at.isformat()
        x_dict["__class__"] = self.__class__.__name__
        return x_dict
