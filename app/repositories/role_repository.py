from sqlalchemy.orm import Session
from app.dtos.role_dto import CreateRoleDto
from app.models.role import Role


class RoleRepository:
    @staticmethod
    def create_role(db, roleDto: CreateRoleDto):
        newRole = Role(name= roleDto.name)
        db.add(newRole)
        db.commit()
        db.refresh(newRole)
        return newRole
    @staticmethod
    def get_role_by_name(db, name: str):
        return db.query(Role).filter(Role.name == name).first()
    @staticmethod
    def get_all(db: Session):
        return db.query(Role).all()
    
    @staticmethod
    def create(db: Session, role: Role):
        db.add(role)
        db.commit()
        db.refresh(role)
        return role