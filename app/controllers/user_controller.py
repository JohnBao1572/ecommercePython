from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.dtos.user_dto import LoginUserDto, RegisterUserDto, UserResponseDto
from app.services.user_service import UserService
from app.utils.response_helper import response


router = APIRouter(prefix="/users", tags=["Users"])
@router.post("/register")
def register(user: RegisterUserDto, db: Session = Depends(get_db)):
    newuser = UserService.register(db, user)
    return response(True, "User registered successfully", {
        "id": newuser.id,
        "name": newuser.name,
        "email": newuser.email
    }, 200)
@router.post("/login")
def login(user: LoginUserDto, db: Session = Depends(get_db)):
    loginUser = UserService.login(db, user)
    return response(True, "User login success", {
        "id": loginUser["user"].id,
        "name": loginUser["user"].name,
        "email": loginUser["user"].email,
        "access_token": loginUser["access_token"],   
        "refresh_token": loginUser["refresh_token"] 
    }, 200)

