import datetime
import uuid
from enum import StrEnum
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import UUID

from .accounts import Accounts
from .base import Base
from .loan import Loan
from .user_session import UserSession


class IdentityVerificationStatus(StrEnum):
  unverified = "unverified"
  pending = "pending"
  verified = "verified"
  failed = "failed"

def get_display_name(self) -> str:
  return {
      IdentityVerificationStatus.unverified: "Unverified",
      IdentityVerificationStatus.pending: "Pending",
      IdentityVerificationStatus.verified: "Verified",
      IdentityVerificationStatus.failed: "Failed",
  }[self]

class User(Base):
  __tablename__ = 'users'
  id = Column(UUID, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  fullname = Column(String)
  phone_number = Column(String)
  recovery_email = Column(String, nullable=True)
  created_at = Column(String, default=datetime.datetime.utcnow())
  active = Column(Boolean, default=True)
  superuser = Column(Boolean, default=False)
  email_verified = Column(Boolean, nullable=False, default=False)
  verified = Column(Boolean, default=False)
  
  
  
  accounts = relationship("Accounts", back_populates="user")
