#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity inherits from BaseModel and Base"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary=place_amenity,
                          back_populate="amenities")
