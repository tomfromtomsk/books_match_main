# Вот пример кода для заполнения базы данных тестовыми данными:

# Импортируем модуль sqlite3
import sqlite3

# Создаем подключение к файлу базы данных
conn = sqlite3.connect('books.db')

# Создаем курсор для выполнения SQL-запросов
cur = conn.cursor()

# Вставляем тестовые данные в таблицу books
cur.execute('''
INSERT INTO books (title, author, genre, description) VALUES
('1984', 'George Orwell', 'Dystopia', 'A novel about a totalitarian society where Big Brother is watching you.'),
('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 'A comedy series about the adventures of Arthur Dent in the galaxy.'),
('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-age', 'A novel about the rebellious teenager Holden Caulfield and his quest for identity.'),
('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 'Fantasy', 'The first book of the famous series about the young wizard Harry Potter and his friends at Hogwarts School of Witchcraft and Wizardry.'),
('The Da Vinci Code', 'Dan Brown', 'Thriller', 'A novel about the symbologist Robert Langdon and his investigation of a murder linked to a secret society and a religious mystery.')
''')

# Вставляем тестовые данные в таблицу users
cur.execute('''
INSERT INTO users (name) VALUES
('Alice'),
('Bob'),
('Charlie'),
('David'),
('Eve')
''')

# Вставляем тестовые данные в таблицу reviews
cur.execute('''
INSERT INTO reviews (user_id, book_id, rating, comment) VALUES
(1, 1, 5, 'A masterpiece of dystopian fiction.'),
(1, 2, 4, 'Very funny and witty.'),
(2, 1, 3, 'A bit depressing but well-written.'),
(2, 3, 4, 'I can relate to Holden Caulfield.'),
(3, 2, 5, 'My favorite book of all time.'),
(3, 4, 5, 'A magical story that captivated me from the start.'),
(4, 3, 2, 'I did not like the main character or his attitude.'),
(4, 5, 4, 'A fast-paced and intriguing thriller.'),
(5, 4, 3, 'A good fantasy book but not very original.'),
(5, 5, 5, 'A brilliant and fascinating novel that kept me guessing.')
''')

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем подключение к базе данных
conn.close()