from pydantic import BaseModel, EmailStr


class RegisterUserDto(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginUserDto(BaseModel):
    email: EmailStr
    password: str

class UserResponseDto(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True