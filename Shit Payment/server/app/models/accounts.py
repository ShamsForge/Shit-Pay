from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import Base


class User(Base):
  __tablename__ = 'accounts'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  shit_id = Column(String, unique=True, index=True)
  balance = Column(Integer, default=0)
  active = Column(Boolean, default=True)
  account_type = Column(String, ")

