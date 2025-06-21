from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User

class Transaction(Base):
  __tablename__ = 'transactions'
  
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  transaction_id = Column(String, unique=True, index=True)
  amount = Column(Integer, default=0)
  transaction_type = Column(String, default="None")
  transaction_date = Column(String, default="None")
  