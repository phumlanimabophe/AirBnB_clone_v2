#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import Base

class Place(BaseModel, Base):
    """Place class"""
    __tablename__ = 'places'
    # ... (other attributes)

    # Add the association with Amenity
    amenities = relationship("Amenity",
                            secondary=association_table,
                            viewonly=False,
                            back_populates="place_amenities")

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        return self.amenities

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute for amenities"""
        if isinstance(amenity, Amenity):
            self.amenities.append(amenity)
