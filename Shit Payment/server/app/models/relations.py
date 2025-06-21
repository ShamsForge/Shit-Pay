'''from sqlalchemy.orm import relationship

from .accounts import Accounts
from .users import User

# Define relationships
User.accounts = relationship("Accounts", 
                             back_populates="user", 
                             foreign_keys=[Accounts.user_id])

Accounts.user = relationship("User", 
                            back_populates="accounts")
                            '''