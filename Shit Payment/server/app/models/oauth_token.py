from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .users import User  # For the foreign key relationship


class OAuthToken(Base):
    __tablename__ = "oauth_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider = Column(String, nullable=False)  # e.g., "google", "github"
    access_token = Column(String, nullable=False)  # The OAuth access token
    refresh_token = Column(String, nullable=True)  # Optional refresh token
    expires_at = Column(DateTime, nullable=False)  # When the token expires
    created_at = Column(DateTime, default=datetime.utcnow)  # When the token was created

    # Relationship
    user = relationship("User", back_populates="oauth_tokens")