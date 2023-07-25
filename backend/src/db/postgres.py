from contextlib import contextmanager
from typing import Iterator

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from pydantic import BaseSettings, Field


@contextmanager
def get_postgres(**dsn) -> Iterator[_connection]:
    """
    Функция с контекстным менеджером для подключении к базе данных SQLite.

    Args:
        dsn: Параметры для подключения к базе данных (Data Source Name)

    Yields:
        _connection: Соединение с базой данных
    """
    conn = psycopg2.connect(**dsn)
    conn.cursor_factory = DictCursor
    yield conn
    conn.close()


class PostgresSettings(BaseSettings):
    """Класс для валидации настроек подключения к PostgreSQL."""

    dbname: str = Field(default='movies_database', env='postgres_db')
    user: str = Field(default='postgres', env='postgres_user')
    password: str = Field(default='postgres', env='postgres_password')
    host: str = Field(default='localhost', env='postgres_host')
    port: int = Field(default=5432, env='postgres_port')
    options: str = Field(default='-c search_path=content')
