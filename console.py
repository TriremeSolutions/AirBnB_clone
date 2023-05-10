#!/usr/bin/env python3
"""
Console for AirBnB clone
"""

import cmd
from models import storage
from models.base_model import BaseModel
import json
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def_class = ['BaseModel']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        else:
            n_dict = {'BaseModel': BaseModel}
            my_model = n_dict[arg]()
            print(my_model.id)
            my_model.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
