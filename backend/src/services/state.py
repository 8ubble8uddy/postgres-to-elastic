import abc
import json
from typing import Any, Dict

from pydantic.dataclasses import dataclass
from redis import Redis

from services.base import Config


class BaseStorage(object):
    """Базовый класс для постоянного хранилища."""

    @abc.abstractmethod
    def save_state(self, state: Dict) -> None:
        """Сохраняет состояние в постоянное хранилище.

        Args:
            state: Новое состояние.
        """

    @abc.abstractmethod
    def retrieve_state(self) -> Dict:
        """Загружает состояние локально из постоянного хранилища."""


@dataclass(config=Config)
class RedisStorage(BaseStorage):
    """Класс для хранения данных в формате JSON."""

    redis_adapter: Redis

    def __post_init__(self):
        """При инициализации запрашивает и получает данные из Redis под ключом `data`."""
        self.data = self.redis_adapter.get('data')

    def save_state(self, state: Dict) -> None:
        """Сохраняет состояние в виде строки.

        - получает состояние с данными в виде словаря;
        - конвертирует словарь в строку;
        - записывает строку в хранилище Redis под ключ `data`.

        Args:
            state: Новое состояние в виде словаря.
        """
        self.redis_adapter.set('data', json.dumps(state, default=str))

    def retrieve_state(self) -> Dict:
        """Загружает состояние в виде словаря.

        - загружает состояние c данными из хранилище Redis под ключом `data` в виде строки;
        - конвертирует строку в словарь;
        - если нет данных возвращает пустой словарь.

        Returns:
            Dict: Текущее состояние в виде словаря.
        """
        return json.loads(self.data) if self.data else {}


@dataclass(config=Config)
class State(object):
    """Класс для хранения состояния при работе с данными."""

    storage: BaseStorage

    def __post_init__(self):
        """При инициализации загружает данные текущего состояния."""
        self.data = self.storage.retrieve_state()

    def write_state(self, key: str, value: Any) -> None:
        """Устанавливает состояние для определённого ключа.

        Args:
            key: Ключ
            value: Значение
        """
        self.data[key] = value
        self.storage.save_state(self.data)

    def read_state(self, key: str, default: Any = None) -> Any:
        """Получает состояние по определённому ключу.

        Args:
            key: Ключ.
            default: Значение, если нет ключа.

        Returns:
            Any: Значение по ключу.
        """
        return self.data.get(key, default)
