from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base


class Upazila(Base):
    __tablename__ = "upazilas"

    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=False)
    upazila_name = Column(String(100), nullable=False)