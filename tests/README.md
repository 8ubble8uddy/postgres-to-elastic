### **Как запустить тесты:**

Клонировать репозиторий и перейти внутри него в директорию ```/tests```:
```
git clone https://github.com/8ubble8uddy/postgres-to-elastic.git
```
```
cd postgres-to-elastic/tests/
```

Создать файл .env и добавить настройки для тестов:
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

Развернуть и запустить тесты в контейнерах:
```
docker-compose up --build --exit-code-from tests
```

### Автор: Герман Сизов