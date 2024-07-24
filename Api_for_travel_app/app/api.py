from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schema, database

router = APIRouter()

@router.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(database.SessionLocal)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(database.SessionLocal)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/destinations/", response_model=schema.Destination)
def create_destination(destination: schema.DestinationCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_destination(db=db, destination=destination)

@router.get("/destinations/", response_model=list[schema.Destination])
def read_destinations(skip: int = 0, limit: int = 10, db: Session = Depends(database.SessionLocal)):
    destinations = crud.get_destinations(db, skip=skip, limit=limit)
    return destinations

@router.post("/itineraries/", response_model=schema.Itinerary)
def create_itinerary(itinerary: schema.ItineraryCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_itinerary(db=db, itinerary=itinerary)
