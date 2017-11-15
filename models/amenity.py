#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.place import place_amenity, Place

class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_type == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
