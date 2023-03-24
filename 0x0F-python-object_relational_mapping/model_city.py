#!/usr/bin/python3
"""Class definition of a city with declaration of base"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """A class that defines props of a City which is mapped to the\
    cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)
# Base.metadata.create_all(engine)
