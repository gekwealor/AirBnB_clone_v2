#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """This class defines  user by various attributes
       "Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user",
                          cascade='all, delete, delete-orphan')
    reviews = relationship("Review", backref="user",
                           cascade='all, delete, delete-orphan')
