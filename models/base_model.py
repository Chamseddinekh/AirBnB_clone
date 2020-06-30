#!/usr/bin/python3
""" base class for all """
import uuid
import datetime


class BaseModel():
    """Basemodel constructor"""


    def __init__(self, *args, **kwargs):
        if kwargs is not {}:
            for arg in kwargs:
                if arg == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
                elif arg == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                        self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[arg] = kwargs[arg]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        BaseModel str method
        """


        return ("{}{}{}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        public instance attribute updated_at with the current datetime
        """


        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Method eturns a dictionary containing all keys/values
        """


        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict['created_at'] = new_dict["created_at"].isoformat()
        new_dict['updated_at'] = new_dict["updated_at"].isoformat()
        return new_dict
