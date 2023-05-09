import json
import os.path
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects


