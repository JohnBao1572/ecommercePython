from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.dtos.auth_dto import LoginAuthDto, RegisterAuthDto
from app.services.auth_service import AuthService
from app.utils.response_helper import response


router = APIRouter(prefix="/auths", tags=["Auths"])
@router.post("/register")
def register(auth: RegisterAuthDto, db: Session = Depends(get_db)):
    newAuth = AuthService.registerAuth(db, auth)
    return response(True, "Auth register success", {
        "id": newAuth.id,
        "name": newAuth.name,
        "email": newAuth.email,
        "role_id": newAuth.role_id
    }, 200)
@router.post("/login")
def login(user: LoginAuthDto, db: Session = Depends(get_db)):
    loginAuth = AuthService.login(db, user)
    return response(True, "Auth login successs", {
        "id": loginAuth["user"].id,
        "name": loginAuth["user"].name,
        "email": loginAuth["user"].email,
        "role_id": loginAuth["user"].role_id,
        "access_token": loginAuth["access_token"],   
        "refresh_token": loginAuth["refresh_token"] 
    })