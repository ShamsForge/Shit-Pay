import pydantic
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.util import typing

from .database import Base


class User(Base):
    __tablename__ = 'users',
  
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    active = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)


class Bank(Base):
    __tablename__ = 'bank'
  
    #items = relationship("Item", back_populates="owner")
    #transactions = relationship("Transaction", back_populates="owner")
    accounts = relationship("Account", back_populates="owner")
    cards = relationship("Card", back_populates="owner")
    loans = relationship("Loan", back_populates="owner")
    savings = relationship("Saving", back_populates="owner")
    investments = relationship("Investment", back_populates="owner")
    insurance = relationship("Insurance", back_populates="owner")
    real_estate = relationship("RealEstate", back_populates="owner")
    vehicles = relationship("Vehicle", back_populates="owner")
    utilities = relationship("Utility", back_populates="owner")
    bills = relationship("Bill", back_populates="owner")
    subscriptions = relationship("Subscription", back_populates="owner")
    donations = relationship("Donation", back_populates="owner")
    gifts = relationship("Gift", back_populates="owner")
    other_income = relationship("OtherIncome", back_populates="owner")