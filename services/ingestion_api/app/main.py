from fastapi import FastAPI
from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

print("Загрузка main.py и инициализация FastAPI приложения...")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Log Ingestion API"}


class LogEntry(BaseModel):
    timestamp: datetime
    service_name: str
    level: str
    message: str


#... import LogEntry...

app = FastAPI()

@app.post("/logs", status_code=status.HTTP_201_CREATED)
async def ingest_log(log: LogEntry):
    print(f"Received log: {log.model_dump()}")
    # В будущем здесь будет отправка в очередь/хранилище
    return {"status": "log received"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

print("main.py загружен, эндпоинты определены.")
