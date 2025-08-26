from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.dtos.auth_dto import LoginAuthDto, RegisterAuthDto
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.jwt_helper import create_access_token, create_refresh_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def registerAuth(db:Session, authDto: RegisterAuthDto):
        existsUser = UserRepository.get_user_by_email(db, authDto.email)
        if existsUser:
            raise HTTPException(status_code=400, detail="EMail has aldready")
        hassPassword = pwd_context.hash(authDto.password)
        newUser = User(
            name= authDto.name,
            email=authDto.email,
            password=hassPassword,
            role_id = authDto.role_id
        )
        return UserRepository.create(db, newUser)
    @staticmethod
    def login(db:Session, loginDto: LoginAuthDto):
        user = UserRepository.get_user_by_email(db, loginDto.email)
        if not user or not pwd_context.verify(loginDto.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid compare or not found this email")
        payload = {"sub": str(user.id), "email": user.email}
        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        return {"user": user,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
