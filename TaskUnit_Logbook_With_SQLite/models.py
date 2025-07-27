from sqlalchemy import Column, Integer, String, Float
from database import Base

class LogEntry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120))
    body = Column(String)
    isoTime = Column(String)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
