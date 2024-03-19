#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy.orm import relationship
import models
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
     if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """a list of all related City objects"""
            cities = list()
            for city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
