import datetime
import uuid
from enum import StrEnum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import Base


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
  id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
  uuid = Column(default_factory=uuid.uuid4, primary_key=True, unique=True)
  shit_id = Column(String, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  fullname = Column(String, nullable=True)
  country_code = Column(String)
  phone_number = Column(String)
  recovery_email = Column(String, nullable=True)
  created_at = Column(String, default=datetime.datetime.now(datetime.UTC))
  active = Column(Boolean, default=True)
  superuser = Column(Boolean, default=False)
  email_verified = Column(Boolean, nullable=False, default=False)
  verified = Column(get_display_name = None)
  
  
