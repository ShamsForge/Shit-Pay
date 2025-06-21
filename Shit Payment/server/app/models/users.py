import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .accounts import Accounts
from .base import Base
from .loan import Loan
from .oauth_token import OAuthToken
from .two_factor_auth import TwoFactorAuth
from .user_session import UserSession


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  display_name = Column(String)
  phone_number = Column(String)
  recovery_email = Column(String, nullable=True)
  created_at = Column(String, default=datetime.datetime.utcnow())
  active = Column(Boolean, default=True)
  superuser = Column(Boolean, default=False)
  verified = Column(Boolean, default=False)
  
  
  accounts = relationship("Accounts", back_populates="user")
  sessions = relationship("UserSession", back_populates="user")
  two_factor_auth = relationship("TwoFactorAuth", back_populates="user", uselist=False)
  oauth_tokens = relationship("OAuthToken", back_populates="user")
  loans = relationship("Loan", back_populates="user")