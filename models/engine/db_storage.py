#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        '''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}

        if cls is not None and cls != '':
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        '''
            Add object to current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit all changes of current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Delete from current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Commit all changes of current database session
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        '''
            Remove private session attribute
        '''
        self.__session.close()

    def get(self, cls, id):
        '''
        gets an object
        Args:
            cls (str): class name
            id (str): object ID
        Returns:
            an object based on class name and its ID
        '''
        obj_dict = models.storage.all(cls)
        for k, v in obj_dict.items():
            matchstring = cls + '.' + id
            if k == matchstring:
                return v

        return None

    def count(self, cls=None):
        '''
        counts number of objects of a class (if given)
        Args:
            cls (str): class name
        Returns:
            number of objects in class, if no class name given
            return total number of objects in database
        '''
        obj_dict = models.storage.all(cls)
        return len(obj_dict)