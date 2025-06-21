from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import Base


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  display_name = Column(String)
  phone_number = Column(String)
  recovery_email = Column(String, nullable=True)
  active = Column(Boolean, default=True)
  superuser = Column(Boolean, default=False)
