# Использовать официальный базовый образ Python
FROM python:3.9-slim

# Установить рабочую директорию в контейнере
WORKDIR /app

# Скопировать файл зависимостей
COPY requirements.txt requirements.txt

# Установить зависимости, не кешируя их
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать код приложения в рабочую директорию
COPY ./app /app

# Открыть порт, на котором будет работать API
EXPOSE 8000

# Команда для запуска приложения при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
