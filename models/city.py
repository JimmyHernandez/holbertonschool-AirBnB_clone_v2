#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    """This is a Python class that inherits from two other classes/
       BaseModel and Base, and represents a
       city."""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
   
    if environ.get("HBNB_TYPE_STORAGE"):
        places = relationship(
        'Place', cascade='all, delete-orphan', backref='cities')
