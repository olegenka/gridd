# Docker Containers Network with SQLite

Этот проект демонстрирует работу двух Docker-контейнеров:
1. Контейнер с базой данных SQLite
2. Контейнер с веб-приложением на Flask

## Структура проекта

```
.
├── db/
│   ├── Dockerfile
│   └── init_db.py
├── app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:
```powershell
git clone <repository-url>
cd <repository-name>
```

2. Запустите контейнеры:
```powershell
docker-compose up --build
```

3. Приложение будет доступно по адресу: http://localhost:5000

## API Endpoints

### GET /users
Получение списка всех пользователей:
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/users" -Method Get
```

### POST /users
Создание нового пользователя:
```powershell
$body = @{
    name = "New User"
    email = "new@example.com"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/users" -Method Post -Body $body -ContentType "application/json"
```

### GET /messages
Получение списка всех сообщений:
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/messages" -Method Get
```

## Особенности

- Данные сохраняются между перезапусками контейнеров благодаря использованию Docker volumes
- Контейнеры автоматически перезапускаются при сбоях
- База данных инициализируется при первом запуске
- Используется именованная сеть для изоляции контейнеров
- Контейнеры имеют фиксированные имена для удобства отладки 