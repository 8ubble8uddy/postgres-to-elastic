from typing import ClassVar

from pydantic import Field

from models.base import UUIDMixin


class Person(UUIDMixin):
    """Класс для валидации данных персоны."""

    full_name: str = Field(alias='name')
    _index: ClassVar[str] = 'persons'

    class Config(object):
        """Конфигурация класса персон."""

        allow_population_by_field_name = True
