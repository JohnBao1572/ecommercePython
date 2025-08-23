from app.models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    @staticmethod
    def get_user_by_email(db, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create(db: Session, user:User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user