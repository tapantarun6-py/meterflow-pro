from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))