#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", cascade='all, delete', backref='state')
    
    @property
    def cities(self):
        return self.cities
