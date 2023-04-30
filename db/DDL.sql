# Этот код создает три таблицы: books, users и reviews. Таблица books хранит информацию о книгах, такую как название, автор, жанр и год издания. Таблица users хранит информацию о пользователях, такую как имя пользователя, электронная почта и пароль. Таблица reviews хранит информацию об отзывах пользователей на книги, такую как идентификатор книги, идентификатор пользователя, рейтинг, комментарий и дата. Также в этом коде определены связи между таблицами с помощью внешних ключей.

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  genre VARCHAR(255),
  year INT
);

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE reviews (
  review_id INT PRIMARY KEY,
  book_id INT NOT NULL,
  user_id INT NOT NULL,
  rating INT CHECK (rating BETWEEN 1 AND 5),
  comment TEXT,
  date DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY (book_id) REFERENCES books (book_id),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);


