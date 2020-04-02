#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            lcities = []
            dcities = models.Storage.all(City)
            for city in dcities.items():
                if city.state_id == self.id:
                    lcities.append(city)
            return lcities
