#!/usr/bin/env python3
"""
Console for AirBnB clone
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
