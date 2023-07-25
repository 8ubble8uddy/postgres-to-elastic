from pydantic import BaseSettings, Field
from redis import Redis


def get_redis(db: int, host: str, port: int) -> Redis:
    """
    Функция для подключения к базе данных Redis.

    Args:
        db: Номер базы данных
        host: Хост для подключения к базе данных
        port: Порт

    Returns:
        Redis: Соединение с базой данных
    """
    return Redis(db=db, host=host, port=port)


class RedisSettings(BaseSettings):
    """Класс для валидации настроек подключения к Redis."""

    db: int = Field(default=0)
    host: str = Field(default='localhost', env='redis_host')
    port: int = Field(default=6379, env='redis_port')
