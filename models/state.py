#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage, storage_type
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            return [city for city in storage.all(City) if city.state_id == self.id]
    def __init__(self, *args, **kwargs):
        """Class for states."""
        super().__init__(*args, **kwargs)
