from typing import ClassVar

from models.base import UUIDMixin


class Genre(UUIDMixin):
    """Класс для валидации данных жанра."""

    name: str
    description: str
    _index: ClassVar[str] = 'genres'
