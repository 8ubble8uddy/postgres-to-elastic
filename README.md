## PostgreSQL to Elasticsearch

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/8ubble8uddy/postgres-to-elastic/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/8ubble8uddy/postgres_to_elastic)
[![last updated](https://img.shields.io/static/v1?label=last%20updated&message=september%202022&color=yellow)](https://img.shields.io/static/v1?label=last%20updated&message=september%202022&color=yellow)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/8ubble8uddy/postgres-to-elastic/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![tests](https://img.shields.io/static/v1?label=tests&message=%E2%9C%94%207%20|%20%E2%9C%98%200&color=critical)](https://github.com/8ubble8uddy/postgres-to-elastic/actions/workflows/main.yml)

### **Описание**

_Целью данного проекта является реализация ETL-скрипта на [Python](https://www.python.org) для синхронизации данных из БД [PostgreSQL](https://www.postgresql.org) в поисковый движок [Elasticsearch](https://www.elastic.co). Данные содержат информацию о фильмах и связанных с ними людях. Отказоустойчивость процесса обеспечивается перехватом ошибок падения хранилищ с применением техники backoff, суть которой в снижении потока запросов при восстановлении соединения. Также программа сохраняет состояние системы, чтобы при перезапуске продолжать работу с места остановки, а не начинать процесс заново. Для проверки получения определённых фильмов на заданный запрос написан набор [Postman](https://www.postman.com)-тестов._

### **Технологии**

```Python``` ```PostgreSQL``` ```Elasticsearch``` ```Redis``` ```Pydantic``` ```Postman``` ```Docker```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```/infra```:
```
git clone https://github.com/8ubble8uddy/postgres-to-elastic.git
```
```
cd postgres-to-elastic/infra/
```

Создать файл .env и добавить настройки для проекта:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=movies_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Elasticsearch
ELASTIC_HOST=elastic
ELASTIC_PORT=9200

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
```

Развернуть и запустить проект в контейнерах:
```
docker-compose up
```

Вместе с Elasticsearch запускается связанный с ним веб-интерфейс для визуализации данных [Kibana](https://www.pgadmin.org):
```
http://127.0.0.1:5601
```

### Автор: Герман Сизов