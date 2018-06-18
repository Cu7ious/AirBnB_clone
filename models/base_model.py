#!/usr/bin/python3
""" The base class for Model
"""
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """ Base class of the models
    """
    def __init__(self):
        """ Constructor of the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Human readable representation of the instance
        """
        cls_name = __class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """ Saves the updates of the state of model
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        """
        raw_dict = self.__dict__
        raw_dict['__class__'] = __class__.__name__
        raw_dict['created_at'] = self.created_at.isoformat()
        raw_dict['updated_at'] = self.updated_at.isoformat()

        return raw_dict
