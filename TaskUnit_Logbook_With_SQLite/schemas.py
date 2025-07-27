from pydantic import BaseModel
from typing import Optional

class LogEntryCreate(BaseModel):
    title: str
    body: str
    lat: Optional[float] = None
    lon: Optional[float] = None

class LogEntryResponse(LogEntryCreate):
    id: int
    isoTime: str