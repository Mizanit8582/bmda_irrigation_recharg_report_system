from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), nullable=False, unique=True)

    password = Column(String(100), nullable=False)

    role = Column(String(50), nullable=False)

    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=True)