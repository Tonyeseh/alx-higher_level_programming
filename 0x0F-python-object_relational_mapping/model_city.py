#!/usr/bin/python3
"""
Contains the declaration of City class and instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()

class City(Base):
    """Defiens the class City for mysql db

        __tablename__ (str): db table name
        id (sqlalchemy.Integer): id column
        name (sqlalchemy.String): name of city
        state_id (sqlalchemy.Integer): foreign key to state table
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
