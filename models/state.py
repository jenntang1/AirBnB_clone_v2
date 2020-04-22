#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
import os
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        name = ''

        @property
        def cities(self):
            """
            Getter that returns cities
            """
            new_list = []
            all_entries = models.storage.all()
            for key, value in all_entries.items():
                split_key = entry.split('.')
                if split_key[1] == self.id:
                    new_list.append(value)

            return new_list
    else:
        name = Column("name", String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref='state')
