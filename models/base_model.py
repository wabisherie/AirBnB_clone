#!/usr/bin/python3
import uuid
from datetime import datetime
import models
import storage

class BaseModel:

    """The base class for our application called hbnb"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs[created_at]
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs[updated_at]
                                                    "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = uuid.uuid4()
            print(f"{self.id}")
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ function str to return the class name id and
        dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """save function to keep the updated at time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ the dictionary function to return the created dictionary"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
