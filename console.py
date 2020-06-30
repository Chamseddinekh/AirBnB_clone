#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    my_classes = {'BaseModel': BaseModel}
    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        return True
    def emptyline(self):
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()