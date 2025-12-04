from typing import TypeVar, Generic, List, Optional
from repositories.base_repository import BaseRepository

T = TypeVar("T")

class BaseServiceImpl(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self.repository.get_all(skip, limit)

    def get_by_id(self, id: int) -> Optional[T]:
        return self.repository.get_by_id(id)

    def create(self, entity: T) -> T:
        return self.repository.create(entity)

    def update(self, id: int, entity_data: dict) -> Optional[T]:
        return self.repository.update(id, entity_data)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
