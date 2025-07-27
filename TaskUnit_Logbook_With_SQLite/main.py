from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas
from database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Optional: allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return "OK"

@app.get("/entries", response_model=list[schemas.LogEntryResponse])
def get_all_entries(db: Session = Depends(get_db)):
    return db.query(models.LogEntry).order_by(models.LogEntry.id.desc()).all()

@app.get("/entries/{entry_id}", response_model=schemas.LogEntryResponse)
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(models.LogEntry).filter(models.LogEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@app.post("/entries", response_model=schemas.LogEntryResponse)
def create_entry(new_entry: schemas.LogEntryCreate, db: Session = Depends(get_db)):
    iso_time = datetime.utcnow().isoformat() + "Z"
    entry = models.LogEntry(
        title=new_entry.title,
        body=new_entry.body,
        isoTime=iso_time,
        lat=new_entry.lat,
        lon=new_entry.lon,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
