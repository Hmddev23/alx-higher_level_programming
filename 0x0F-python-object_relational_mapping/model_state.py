#!/usr/bin/python3
"""
define the class State class and
the Base class from MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    define the State class

    Attributes:
        __tablename__ (str): The class table name of .
        id (int): The class State id.
        name (str): The class State name.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
