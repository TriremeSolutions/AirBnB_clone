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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        if not arg:
            print("** class name missing **")
            return

        spl_arg = arg.split(' ')

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        elif len(spl_arg) == 1:
            print("** instance id missing **")
        else:
            obj_tot = storage.all()
            for key, value in obj_tot.items():
                name_obj = value.__class__.__name__
                id_obj = value.id
                if name_obj == spl_arg[0] and id_obj == spl_arg[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Change is saved into the JSON file
        """
        if not arg:
            print("** class name missing **")
            return

        spl_arg = arg.split(' ')

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        elif len(spl_arg) == 1:
            print("** instance id missing **")
        else:
            obj_tot = storage.all()
            for key, value in obj_tot.items():
                name_obj = value.__class__.__name__
                id_obj = value.id
                if name_obj == spl_arg[0] and id_obj == spl_arg[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
