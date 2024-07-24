# app/schema.py
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class DestinationBase(BaseModel):
    name: str
    description: Optional[str] = None
    country: str
    city: str

class DestinationCreate(DestinationBase):
    pass

class Destination(DestinationBase):
    id: int

    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    user_id: int
    destination_id: int
    start_date: str
    end_date: str
    total_cost: Optional[float] = None

class ItineraryCreate(ItineraryBase):
    pass

class Itinerary(ItineraryBase):
    id: int

    class Config:
        orm_mode = True
