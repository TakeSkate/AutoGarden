from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base


class Registry(Base):
    __tablename__ = "registry"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String(2), index=True)
    month = Column(String(2), index=True)
    year = Column(String(4), index=True)
    hour = Column(String(2), index=True)
    minute = Column(String(2), index=True)
    temperatura_ambiente = Column(Integer, index=True)
    humedad_ambiente = Column(Integer, index=True)
    humedad_planta = Column(Integer, index=True)
    luminosidad = Column(Integer, index=True)
    riego = Column(Boolean, default=0, index=True)
