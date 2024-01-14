#!/usr/bin/python3
"""
define a City class to work with MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class definition

    Attributes:
        __tablename__ (str): Name of the class table
        id (int): Id of the class
        name (str): Name of the class
        state_id (int): State the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
