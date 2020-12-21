#!/usr/bin/python3
"""hat contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Consol class"""

    prompt = '(hbnb)'
    my_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                  'City': City, 'Amenity': Amenity, 'Place': Place,
                  'Review': Review}

    def do_quit(self, arg):
        """quit console"""
        return True

    def do_EOF(self, arg):
        """quit console with EOF"""
        return True

    def emptyline(self):
        """handle emptyline"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
