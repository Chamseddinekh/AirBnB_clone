#!/usr/bin/python3
"""hat contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Consol class"""

    prompt = '(hbnb)'
    my_classes = {'BaseModel': BaseModel, 'User': User}

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
