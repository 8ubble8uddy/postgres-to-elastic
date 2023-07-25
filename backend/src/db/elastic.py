from elasticsearch import Elasticsearch
from pydantic import BaseSettings, Field


def get_elastic(host: str, port: int) -> Elasticsearch:
    """
    Функция для подключения к базе данных Elasticsearch.

    Args:
        host: Узел для подключения к базе данных
        port: Порт

    Returns:
        Elasticsearch: Соединение с базой данных
    """
    return Elasticsearch(host=host, port=port)


class ElasticSettings(BaseSettings):
    """Класс для валидации настроек подключения к Elasticsearch."""

    host: str = Field(default='localhost', env='elastic_host')
    port: int = Field(default=9200, env='elastic_port')
