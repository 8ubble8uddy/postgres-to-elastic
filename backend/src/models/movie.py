from typing import Any, ClassVar, Dict, List

from pydantic import Field, validator

from models.base import UUIDMixin
from models.person import Person


class Movie(UUIDMixin):
    """Класс для валидации данных фильма."""

    imdb_rating: float
    genre: List[str]
    title: str
    description: str
    director: List[str] = Field(alias='directors_names')
    actors_names: List[str]
    writers_names: List[str]
    actors: List[Person]
    writers: List[Person]
    _index: ClassVar[str] = 'movies'

    @classmethod
    def properties(cls, **kwargs) -> Dict[str, Any]:
        """Возвращает схему модели фильма с её характеристиками.

        Args:
            kwargs: Необязательные именованные аргументы

        Returns:
            Dict: Словарь со схемой модели
        """
        properties: Dict[str, Any] = {}
        for field, value in cls.schema(**kwargs)['properties'].items():
            if value['type'] == 'string':
                properties[field] = ''
            if value['type'] == 'array':
                properties[field] = []
            if value['type'] == 'number':
                properties[field] = 0
        return properties

    @validator('actors', 'writers', each_item=True)
    def change_person_field(cls, person: Person) -> Dict:
        """
        Валидатор для смены названия поля полного имени персоны.

        Args:
            person: Объект персоны

        Returns:
            Dict: Данные персоны для фильма
        """
        return {'id': person.id, 'name': person.full_name}
