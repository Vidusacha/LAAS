from fastapi.testclient import TestClient
from app.main import app # Импортировать экземпляр FastAPI
import pytest
from datetime import datetime

print("Загрузка test_api.py и инициализация TestClient...")

client = TestClient(app)

def test_health_check():
    print("\n--- Начало теста: test_health_check ---")
    print("Отправка запроса на /health...")

    response = client.get("/health")
    print(f"Получен ответ: статус {response.status_code}, тело {response.json()}")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    print("--- Конец теста: test_health_check ---")

def test_ingest_log_success():

    print("\n--- Начало теста: test_ingest_log_success ---")

    log_data = {
        "timestamp": datetime.now().isoformat(),
        "service_name": "test_service",
        "level": "INFO",
        "message": "Test log message"
    }
    print(f"Отправка POST запроса на /logs с данными: {log_data}")

    response = client.post("/logs", json=log_data)
    print(f"Получен ответ: статус {response.status_code}, тело {response.json()}")

    assert response.status_code == 201 # Проверяем статус Created
    assert response.json() == {"status": "log received"}
    print("--- Конец теста: test_ingest_log_success ---")


def test_ingest_log_invalid_data():
    print("\n--- Начало теста: test_ingest_log_invalid_data ---")

    log_data = {
        "timestamp": "not-a-datetime", # Невалидное значение
        "service_name": "test_service",
        "level": "INFO",
        "message": "Test log message"
    }
    print(f"Отправка POST запроса на /logs с невалидными данными: {log_data}")
    response = client.post("/logs", json=log_data)

    print(f"Получен ответ: статус {response.status_code}, тело {response.json()}")
    assert response.status_code == 422 # Unprocessable Entity (ошибка валидации FastAPI/Pydantic)
    print("--- Конец теста: test_ingest_log_invalid_data ---")

    print("test_api.py загружен, тесты определены.")



