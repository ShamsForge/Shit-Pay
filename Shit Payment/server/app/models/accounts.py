from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User


class Accounts(Base):
  __tablename__ = 'accounts'
  
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, 
                   ForeignKey("users.id"),
                   nullable=False)
  shit_id = Column(String, unique=True, index=True)
  balance = Column(Integer, default=0)
  credit_score = Column(Integer, default=0, min=0, max=850)
  account_type = Column(String, default="None")
  active = Column(Boolean, default=True)



  # Relationships
user = relationship("User", back_populates="accounts")