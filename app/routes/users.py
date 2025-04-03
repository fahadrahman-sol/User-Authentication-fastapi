# users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import LoginSchema, TokenSchema, UserCreate, UserResponse
from models import User
from auth import hash_password, login_user, verify_password, create_access_token
from database import get_db

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, phone=user.phone, hashed_password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=TokenSchema)
def login(user_data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(email=user_data.email, password=user_data.password, db=db)