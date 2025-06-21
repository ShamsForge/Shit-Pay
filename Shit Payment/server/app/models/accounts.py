from enum import StrEnum

#from typing import Annotated
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User


class Accounts(Base):
  
  class Status(StrEnum):
        CREATED = "created"
        ONBOARDING_STARTED = "onboarding_started"
        UNDER_REVIEW = "under_review"
        DENIED = "denied"
        ACTIVE = "active"
      

        def get_display_name(self) -> str:
            return {
                Accounts.Status.CREATED: "Created",
                Accounts.Status.ONBOARDING_STARTED: "Onboarding Started",
                Accounts.Status.UNDER_REVIEW: "Under Review",
                Accounts.Status.DENIED: "Denied",
                Accounts.Status.ACTIVE: "Active",
            }[self]
          
  
  __tablename__ = 'accounts'
  
  id = Column(Integer, primary_key=True, index=True)
  shit_id = Column(String, unique=True, index=True)
  balance = Column(Integer, default=0)
  account_limit = Column(Integer, default=10000)
  credit_score = Column(Integer, default=0, min=0, max=850)
  account_type = Column(String, default="None")
  active = Column(Boolean, default=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

  # Relationships
  user = relationship("User", back_populates="accounts")