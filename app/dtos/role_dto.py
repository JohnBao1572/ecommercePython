
from pydantic import BaseModel


class CreateRoleDto(BaseModel):
    name: str

class RoleResponseDto(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True