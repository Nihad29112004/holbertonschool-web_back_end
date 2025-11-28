#!/usr/bin/env python3
""" FileStorage engine """

import json


class FileStorage:
    """serializes objects to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save objects to file"""
        with open(FileStorage.__file_path, "w") as f:
            tmp = {k: v.to_json() for k, v in FileStorage.__objects.items()}
            json.dump(tmp, f)

    def reload(self):
        """reload objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                from models.user import User
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    FileStorage.__objects[k] = User(**v)
        except Exception:
            pass
