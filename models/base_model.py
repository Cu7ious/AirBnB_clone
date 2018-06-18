#!/usr/bin/python3
""" The base class for Model
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base class of the models
    """
    def __init__(self):
        """ Constructor of the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        print(self.id, self.created_at, self.updated_at)

    def __str__(self):
        print("[BaseModel] ({0}) {1}".format(self.id, self.__dict__))

    def save(self):
        """ Saves the updates of the state of model
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        """
        pass

BaseModel()
