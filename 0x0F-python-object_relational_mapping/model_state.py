#!/usr/bin/python3
"""
Contains the declaration of class State and instance Base
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines the class State for mysql db

        __tablename__ (str): name of database to store States
        id (sqlalchemy.Integer): state's id
        name (sqlalchemy.String): state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
