import sqlalchemy
from objects.model import Book
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.engine import URL

# Создаем экземпляр приложения
app = Flask(__name__)

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="books_match_db"
)

db = create_engine(url)
Session = sessionmaker(db)  
session = Session()

# Определяем URL-правила и функции-обработчики для разных типов запросов от бота
@app.route('/')
def index():
    return render_template('index.html')

# Получить список всех книг
@app.route('/books', methods=['GET'])
def get_books():
  books = Book.query.all()
  return jsonify([book.title for book in books])

# Получить информацию о книге по названию
@app.route('/books/<title>', methods=['GET'])
def get_book(title):
  book = Book.query.filter_by(title=title)
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
  app.run(debug=False)