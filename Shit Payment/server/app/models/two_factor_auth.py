from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User  # For the foreign key relationship


class TwoFactorAuth(Base):
    __tablename__ = "two_factor_auth"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)  # One 2FA per user
    method = Column(String, nullable=False)  # e.g., "sms", "authenticator"
    secret = Column(String, nullable=False)  # TOTP secret for authenticator apps
    phone_number = Column(String, nullable=True)  # For SMS 2FA
    is_enabled = Column(Boolean, default=False)  # Whether 2FA is active
    created_at = Column(DateTime, default=datetime.utcnow)  # When 2FA was set up

    # Relationship (one-to-one)
    user = relationship("User", back_populates="two_factor_auth")