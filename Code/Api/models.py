from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Circuit(Base):
    __tablename__ = "circuits"

    circuitId = Column(Integer, primary_key=True, index=True)
    circuitRef = Column(String, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    country = Column(String, index=True)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(String)
