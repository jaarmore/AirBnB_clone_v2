#!/usr/bin/python3
"""This is the place class"""
from os import getenv
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            list_return = []
            for row in list(models.storage.all(Review).values()):
                if row.place_id == self.id:
                    list_return.append(row)
            return list_return

        @property
        def amenities(self):
            list_return = []
            for row in list(models.storage.all(Amenity).values()):
                if row.id in self.amenity_ids:
                    list_return.append(row)
            return list_return

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
    else:
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
