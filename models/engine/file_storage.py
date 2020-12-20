#!/usr/bin/python3
"""
module for serializing and deserializing object to file storage
"""
import os
import json


class FileStorage():
    """
    FileStorage class for serializing and deserializing objects
    into and from files respectively
    """

    engine_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.getcwd()
    __file_path = parent_directory + '/file.json'
    __objects = dict()

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in the obj with key <obj class name>.id"""
        key = str(__class__.__name__)+"."+str(obj.id)
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='UTF8') as f:
            json.dump(new_dict, f)

    def reload(self):
        pass
