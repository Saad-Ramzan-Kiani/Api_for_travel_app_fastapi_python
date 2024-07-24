# app/crud.py
from sqlalchemy.orm import Session
from . import models, schema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schema.UserCreate):
    db_user = models.User(username=user.username, email=user.email, full_name=user.full_name, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_destinations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Destination).offset(skip).limit(limit).all()

def create_destination(db: Session, destination: schema.DestinationCreate):
    db_destination = models.Destination(**destination.dict())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination

def create_itinerary(db: Session, itinerary: schema.ItineraryCreate):
    db_itinerary = models.Itinerary(**itinerary.dict())
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary
