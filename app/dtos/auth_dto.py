from pydantic import BaseModel, EmailStr


class RegisterAuthDto(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: int

class LoginAuthDto(BaseModel):
    email: EmailStr
    password: str

class AuthResponseDto(BaseModel):
    id: int
    name: str
    email: EmailStr
    role_id: int
    class Config:
        orm_mode = True