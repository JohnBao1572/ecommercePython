from fastapi import HTTPException
from app.dtos.category_dto import CreateCategoryDto, UpdateCategoryDto
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
    @staticmethod
    def get_all(db):
        return CategoryRepository.get_all(db)
    @staticmethod
    def get_cat_by_id(db, cat_id: int):
        cat = CategoryRepository.get_id(db, cat_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")
        return cat
    @staticmethod
    def update_cat(db, cat_id: int, categoryDto: UpdateCategoryDto, currentUser:User):
        cat = CategoryRepository.get_id(db, cat_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")
        if currentUser.role.name != "admin":
            raise HTTPException(status_code=403, detail="You are not allow to update")
        updated_cat = CategoryRepository.update(db, cat, categoryDto.dict(exclude_unset=True))
        return updated_cat       
    @staticmethod
    def delete_cat(db, cat_id: int, currentUser:User):
        cat = CategoryRepository.get_id(db, cat_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")
        if currentUser.role.name != "admin":
            raise HTTPException(status_code=403, detail="You are not allow to delete")
        deleted_cat = CategoryRepository.delete(db, cat)
        return deleted_cat
