from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from .base import Base


class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    transaction_id = Column(String, unique=True, index=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String)  # e.g., "deposit", "withdrawal", "transfer"
    timestamp = Column(DateTime, default=datetime.utcnow)