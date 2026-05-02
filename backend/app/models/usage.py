from sqlalchemy import Column, Integer, String
from core.database import Base

class Usage(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True)
    api_key = Column(String)
    count = Column(Integer, default=0)