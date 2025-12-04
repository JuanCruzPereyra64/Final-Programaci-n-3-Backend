from typing import Type, List, Optional, TypeVar, Generic
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository

T = TypeVar("T")

class InstanceNotFoundError(Exception):
    pass

class BaseRepositoryImpl(BaseRepository[T], Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, entity: T) -> T:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, id: int, entity_data: dict) -> Optional[T]:
        db_entity = self.get_by_id(id)
        if not db_entity:
            return None
        
        for key, value in entity_data.items():
            setattr(db_entity, key, value)
            
        self.db.commit()
        self.db.refresh(db_entity)
        return db_entity

    def delete(self, id: int) -> bool:
        db_entity = self.get_by_id(id)
        if not db_entity:
            return False
        
        self.db.delete(db_entity)
        self.db.commit()
        return True
