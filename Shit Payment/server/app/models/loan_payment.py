from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User


class LoanPayment(Base):
  __tablename__ = 'loan_payments'
  
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
  amount = Column(Integer, default=0)
  payment_date = Column(String, default="None")
  