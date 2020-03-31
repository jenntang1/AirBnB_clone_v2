#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
import os
from sqlalchemy.orm import relationship


metadata = Base.metadata

user = Table('place_amenity', metadata,
             Column('place_id', String(60), primary_key=True,
                    ForeignKey('places.id'), nullable=False),
             Column('amenity_id', String(60), primary_key=True,
                    ForeignKey('amenities.id'), nullable=False))


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
    __tablename__ = 'places'

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        name = ''

        @property
        def amenities(self):
            """
            Info
            """
            new_list = []
            all_entries = models.storage.all()
            for key, value in all_entries.items():
                split_key = entry.split('.')
                if split_key[1] == State.id:
                    new_list.append(value)

            return new_list
    else:
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
