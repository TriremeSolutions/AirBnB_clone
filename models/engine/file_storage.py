import json
import os.path
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)
# TODO FIX THE RELOAD FUNCTION KEEP THROWING NameError: name 'models' is not defined
    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    obj_dict = value
                    obj_dict["created_at"] = datetime.datetime.strptime(obj_dict["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict["updated_at"] = datetime.datetime.strptime(obj_dict["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                    module_name = "models.{}".format(cls_name.lower())
                    cls = eval("{}.{}".format(module_name, cls_name))
                    self.__objects[key] = cls(**obj_dict)
