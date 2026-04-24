from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


# --- Request Schemas ---

class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)
    location: Optional[str] = None
    soil_type: Optional[str] = None
    farm_size_acres: Optional[float] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    location: Optional[str] = None
    soil_type: Optional[str] = None
    farm_size_acres: Optional[float] = None


# --- Response Schemas ---

class UserProfile(BaseModel):
    id: UUID
    name: str
    email: str
    location: Optional[str] = None
    soil_type: Optional[str] = None
    farm_size_acres: Optional[float] = None
    role: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserProfile


class MessageResponse(BaseModel):
    message: str
