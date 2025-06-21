from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User


class Transfer(Base):
  __tablename__ = 'transfers'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  transfer_id = Column(String, unique=True, index=True)
  amount = Column(Integer, default=0)
  transfer_type = Column(String, default="None")
  transfer_date = Column(String, default="None")
  transfer_status = Column(String, default="None")
  transfer_from = Column(String, default="None")
  transfer_to = Column(String, default="None")
  transfer_description = Column(String, default="None")
  