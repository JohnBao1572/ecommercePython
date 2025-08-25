from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.dtos.role_dto import CreateRoleDto
from app.services.role_service import RoleService
from app.utils.response_helper import response

router = APIRouter(prefix="/roles", tags=["Roles"])
@router.post("/add")
def add_role(role: CreateRoleDto, db: Session = Depends(get_db)):
    newRole = RoleService.create_role(db, role)
    return response(True, "Role created success", {
        "id": newRole.id,
        "name": newRole.name
    }, 200)