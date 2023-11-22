#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage, storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(String(60), nullable=False, primary_key=True)
    if storage_type == 'db':
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            return [city for city in storage.all(City) if city.state_id == self.id]
    def __init__(self, *args, **kwargs):
        """Class for states."""
        super().__init__(*args, **kwargs)
