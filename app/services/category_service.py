from fastapi import HTTPException
from app.dtos.category_dto import CreateCategoryDto
from app.models.category import Category
from app.models.user import User
from app.repositories.category_repository import CategoryRepository


class CategoryService:
    @staticmethod
    def create_category(db, category: CreateCategoryDto, currentUser:User):
        if currentUser.role.name != "admin":
            raise HTTPException(status_code=403, detail="You are not authorized to create a category")
        newCategory= Category(
            name = category.name,
            description = category.description,
            addedBy = currentUser.id
        )
        return CategoryRepository.create(db, newCategory)

