from app.models.category import Category


class CategoryRepository:
    @staticmethod
    def get_all(db):
        return db.query(Category).all()
    @staticmethod
    def get_id(db, id: int):
        return db.query(Category).filter(Category.id == id).first()
    @staticmethod
    def create(db, category: Category):
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    @staticmethod
    def update(db, category: Category, data: dict):
        for key, value in data.items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
        return category
    @staticmethod
    def delete(db, category: Category):
        db.delete(category)
        db.commit()
        