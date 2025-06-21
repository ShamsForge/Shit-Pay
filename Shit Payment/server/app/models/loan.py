from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User

class Loan(Base):
  __tablename__ = 'loans'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  loan_id = Column(String, unique=True, index=True)
  amount = Column(Integer, default=0)
  interest_rate = Column(Integer, default=0)
  loan_term = Column(Integer, default=0)
  loan_status = Column(String, default="None")
  loan_type = Column(String, default="None")
  loan_date = Column(String, default="None")
  