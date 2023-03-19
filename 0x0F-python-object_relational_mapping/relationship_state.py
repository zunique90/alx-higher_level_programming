#!/usr/bin/python3
"""
This module defines a state Model
"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City


class State(Base):
    """class state"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
