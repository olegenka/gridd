FROM python:3.9-slim

WORKDIR /app

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов приложения
COPY app.py /app/
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install -r requirements.txt

# Запуск приложения
CMD ["python", "app.py"] 