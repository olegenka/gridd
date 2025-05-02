FROM python:3.9-slim

WORKDIR /app

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Создание директории для базы данных
RUN mkdir -p /data

# Копирование скрипта инициализации базы данных
COPY init_db.py /app/

# Запуск скрипта инициализации при старте контейнера
CMD ["python", "init_db.py"] 