import sqlite3
import os

# Путь к файлу базы данных
DB_PATH = '/data/database.db'

# Создаем директорию, если она не существует
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Подключаемся к базе данных
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Вставляем тестовые данные
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", 
               ('Test User', 'test@example.com'))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно инициализирована!") 