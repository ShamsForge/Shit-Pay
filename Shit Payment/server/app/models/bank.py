from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User


class Bank(Base):
  __tablename__ = 'banks'
  id = Column(Integer, primary_key=True, index=True)
  shit_id = Column(String, index=True)
  name = Column(String, unique=True, index=True)

class transfer(Base):
  __tablename__ = 'transfers'

class investments(Base):
  __tablename__ = 'investments'

class Loan(Base):
  __tablename__ = 'loans'
  id = Column(Integer, primary_key=True, index=True)
  loan_id = Column(String, unique=True, index=True)
  amount = Column(Integer, default=0)
  interest_rate = Column(Integer, default=0)
  loan_term = Column(Integer, default=0)
  loan_status = Column(String, default="None")
  loan_type = Column(String, default="None")
  loan_date = Column(String, default="None")



  user = relationship("User", back_populates="loans")
  accounts = relationship("Accounts", back_populates="loans")

