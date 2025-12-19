# main.py
import sqlite3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Проверяем и создаём БД при первом запуске
if not os.path.exists("database/database.db"):
    from db_init import *  # создаст БД и таблицу


# Читаем количество студентов из БД
def get_students_count():
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    conn.close()
    return count


students_count = get_students_count()


# Кастомный обработчик, чтобы подставить данные в HTML
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            with open('templates/index.html', 'r', encoding='utf-8') as f:
                html = f.read()
                html = html.replace('{{ message }}', 'Добро пожаловать в Личный кабинет студента!')
                html = html.replace('{{ count }}', str(students_count))

            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()


if __name__ == '__main__':
    print("Запуск сервера на http://localhost:8000")
    print(f"В базе сейчас студентов: {students_count}")
    HTTPServer(('localhost', 8000), MyHandler).serve_forever()