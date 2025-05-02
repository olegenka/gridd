import sqlite3
import os
import time

# Путь к файлу базы данных
DB_PATH = '/data/database.db'

# Создаем директорию, если она не существует
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Подключаемся к базе данных
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Создаем таблицу пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Создаем таблицу сообщений
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Вставляем тестовые данные
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", 
               ('Test User', 'test@example.com'))

# Получаем ID созданного пользователя
user_id = cursor.lastrowid or 1

# Вставляем тестовое сообщение
cursor.execute("INSERT OR IGNORE INTO messages (user_id, message) VALUES (?, ?)", 
               (user_id, 'Hello, World!'))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно инициализирована!")

# Держим контейнер запущенным
while True:
    time.sleep(1) 