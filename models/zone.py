from sqlalchemy import Column, Integer, String
from database.connection import Base


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    zone_name = Column(String(100), nullable=False)