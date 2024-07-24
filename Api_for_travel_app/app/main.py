from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base, database
from .api import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(api_router, prefix="/api")
