from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.dtos.role_dto import CreateRoleDto
from app.models.role import Role
from app.repositories.role_repository import RoleRepository


class RoleService:
    @staticmethod
    def create_role(db: Session, roleDto: CreateRoleDto):
        exist = RoleRepository.get_role_by_name(db, roleDto.name)
        if exist:
            raise HTTPException(status_code=400, detail="Role already exists")
        newRole = Role(
            name = roleDto.name
        )
        return RoleRepository.create(db, newRole)
    @staticmethod
    def get_roles(db: Session):
        return RoleRepository.get_all(db)