# Импортируем необходимые модули
from objects import objects
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр приложения
app = Flask(__name__)

# Настраиваем подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определяем URL-правила и функции-обработчики для разных типов запросов от бота

# Получить список всех книг
@app.route('/books', methods=['GET'])
def get_books():
  books = Book.query.all()
  return jsonify([book.title for book in books])

# Получить информацию о книге по названию
@app.route('/books/<title>', methods=['GET'])
def get_book(title):
  book = Book.query.filter_by(title=title).first()
  if book:
    return jsonify({
      'title': book.title,
      'author': book.author,
      'genre': book.genre,
      'description': book.description
    })
  else:
    return jsonify({'error': 'Book not found'})

# Запускаем приложение
if __name__ == '__main__':
  app.run(debug=True)
