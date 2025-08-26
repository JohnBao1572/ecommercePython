from typing import Optional
from pydantic import BaseModel


class CreateCategoryDto(BaseModel):
    name: str
    description: Optional[str] = None

class UpdateCategoryDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryResponseDto(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    addedBy: int

    class Config:
        orm_mode = True
