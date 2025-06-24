import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from .base import Base
from .users import User  # For the foreign key relationship


class UserSession(Base):
    __tablename__ = "user_sessions"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(default_factory=uuid.uuid4, primary_key=True, unique=True)
    shit_id = Column(String, ForeignKey(User.shit_id), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, nullable=False,
                   unique=True)  # Session token (e.g., JWT)
    created_at = Column(DateTime,
                        default=datetime.utcnow)  # When session started
    expires_at = Column(DateTime, nullable=False)  # When session expires
    ip_address = Column(String, nullable=True)  # Login IP for security
    device_info = Column(String, nullable=True)  # Device/browser details

