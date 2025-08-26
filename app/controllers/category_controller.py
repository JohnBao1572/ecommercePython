from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.dtos.category_dto import CreateCategoryDto
from app.models.user import User
from app.services.category_service import CategoryService
from app.utils.jwt_helper import get_current_user
from app.utils.response_helper import response  



router = APIRouter(prefix="/categories", tags=["Categories"])
@router.post("/add")
def add_category(addDto: CreateCategoryDto, db: Session = Depends(get_db), currentUser: User= Depends(get_current_user)):
    newCat = CategoryService.create_category(db, addDto, currentUser)
    return response(True, "Category created success",
                    {
                        "id": newCat.id,
                        "name": newCat.name,
                        "description": newCat.description,
                        "user_id": newCat.addedBy
                    }, 200)
@router.get("/getAll")
def get_all(db: Session = Depends(get_db)):
    cat = CategoryService.get_all(db)
    result = [
        {
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "addedBy": c.addedBy
        }
        for c in cat
    ]
    return response(True, "Category sucess", result, 200)
@router.get("/get/{cat_id}")
def get_by_id(cat_id: int, db: Session = Depends(get_db)):
    cat = CategoryService.get_cat_by_id(db, cat_id)
    return response(True, "Get cat by id success", {
        "id": cat.id,
        "name": cat.name,
        "description": cat.description,
        "addedBy": cat.addedBy
    }, 200)
