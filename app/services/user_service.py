from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.dtos.user_dto import LoginUserDto, RegisterUserDto
from app.models.role import Role
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.jwt_helper import create_access_token, create_refresh_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    def register(db: Session, userDto: RegisterUserDto):
        existUser = UserRepository.get_user_by_email(db, userDto.email)
        if existUser:
            raise HTTPException(status_code=400, detail="Email already registered")
        default_role = db.query(Role).filter(Role.name == "user").first()
        if not default_role:
            raise HTTPException(status_code=500, detail="Not found role")
        hashed_password = pwd_context.hash(userDto.password)
        newUser = User(
            name=userDto.name,
            email=userDto.email,
            password=hashed_password,
            role_id = default_role.id
        )
        return UserRepository.create(db, newUser)
    @staticmethod
    def login(db:Session, loginDto: LoginUserDto):
        user = UserRepository.get_user_by_email(db, loginDto.email)
        if not user or not pwd_context.verify(loginDto.password, user.
                                              password):
            raise HTTPException(status_code=400, detail="Invalid compare")
        payload = {"sub": str(user.id), "email": user.email}
        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        return {"user": user, 
                "access_token": access_token, 
                "refresh_token": refresh_token
            }
