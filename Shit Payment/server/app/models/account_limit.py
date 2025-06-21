from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .accounts import Accounts
from .base import Base
from .users import User


class AccountLimit(Base):
  __tablename__ = 'account_limits'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
account_limit = Column(Integer, default=10000)
account_limit_id = Column(Integer, ForeignKey("account_limits.id"), nullable=True)

#relationships
user = relationship("User", back_populates="account_limits")