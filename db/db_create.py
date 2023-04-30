# Вот пример кода для создания базы данных на sqlite:

# Импортируем модуль sqlite3
import sqlite3

# Создаем подключение к файлу базы данных
conn = sqlite3.connect('books.db')

# Создаем курсор для выполнения SQL-запросов
cur = conn.cursor()

# Создаем таблицу books с полями id, title, author, genre и description
cur.execute('''
CREATE TABLE books (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  genre TEXT NOT NULL,
  description TEXT NOT NULL
)
''')

# Создаем таблицу users с полями id и name
cur.execute('''
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
)
''')

# Создаем таблицу reviews с полями user_id, book_id, rating и comment
cur.execute('''
CREATE TABLE reviews (
  user_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  rating INTEGER NOT NULL,
  comment TEXT,
  PRIMARY KEY (user_id, book_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (book_id) REFERENCES books (id)
)
''')

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем подключение к базе данных
conn.close()
```