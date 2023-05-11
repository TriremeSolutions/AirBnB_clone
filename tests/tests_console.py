#!/usr/bin/python3
"""
Defines some unittests for the command interpreter.
"""
import unittest
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class Test_CLI_prompt(unittest.TestCase):
    """
    This concerns testing the console prompts
    based on user input
    """

    def test_message_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_input(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
