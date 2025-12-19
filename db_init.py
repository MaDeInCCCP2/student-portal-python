# db_init.py
import sqlite3
import os

DB_PATH = "database/database.db"

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Добавляем тестового студента
cursor.execute('''
INSERT OR IGNORE INTO students (first_name, last_name, email) 
VALUES ('Иван', 'Иванов', 'ivan@example.com')
''')

conn.commit()
conn.close()
print("База данных и таблица students успешно созданы!")