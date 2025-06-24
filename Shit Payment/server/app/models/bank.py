import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import Base
from .users import User


class Bank(Base):
  __tablename__ = 'banks'
  id = Column(Integer, primary_key=True, index=True)
  uuid = Column(default_factory=uuid.uuid4, primary_key=True, unique=True)
  shit_id = Column(String, ForeignKey(User.shit_id), index=True)
  name = Column(String, unique=True, index=True)

class transfer(Base):
  __tablename__ = 'transfers'
  id = Column(Integer, primary_key=True, index=True)
  money = Column(Integer, default=0)
  money_from = Column(String, default="None")
  money_to = Column(String, default="None")
  transfer_type = Column(String, default="None")
  transfer_date = Column(String, default="None")
  

class investments(Base):
  __tablename__ = 'investments'
  pass

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




