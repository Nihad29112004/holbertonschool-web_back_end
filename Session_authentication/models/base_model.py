#!/usr/bin/env python3
""" BaseModel module """

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ BaseModel class that defines common attributes/methods """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """save updated date"""
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """return dict representation"""
        r = self.__dict__.copy()
        r["__class__"] = self.__class__.__name__
        r["created_at"] = self.created_at.isoformat()
        r["updated_at"] = self.updated_at.isoformat()
        return r
