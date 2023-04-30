# Вот пример кода flask backend на python используя классы Book, User и Review:

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

# Определяем классы Book, User и Review
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  genre = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f'<Book {self.title}>'

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  books = db.relationship('Book', secondary='review', backref='users')

  def __repr__(self):
    return f'<User {self.name}>'

class Review(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
  rating = db.Column(db.Integer, nullable=False)
  comment = db.Column(db.Text, nullable=True)

  def __repr__(self):
    return f'<Review {self.user_id} {self.book_id} {self.rating}>'

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

# Добавить новую книгу в базу данных
@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()
  title = data.get('title')
  author = data.get('author')
  genre = data.get('genre')
  description = data.get('description')
  if title and author and genre and description:
    book = Book(title=title, author=author, genre=genre, description=description)
    db.session.add(book)
    db.session.commit()
    return jsonify({'success': 'Book added'})
  else:
    return jsonify({'error': 'Missing data'})

# Удалить книгу из базы данных по названию
@app.route('/books/<title>', methods=['DELETE'])
def delete_book(title):
  book = Book.query.filter_by(title=title).first()
  if book:
    db.session.delete(book)
    db.session.commit()
    return jsonify({'success': 'Book deleted'})
  else:
    return jsonify({'error': 'Book not found'})

# Получить список всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
  users = User.query.all()
  return jsonify([user.name for user in users])

# Получить информацию о пользователе по имени
@app.route('/users/<name>', methods=['GET'])
def get_user(name):
  user = User.query.filter_by(name=name).first()
  if user:
    return jsonify({
      'name': user.name,
      'books': [book.title for book in user.books]
    })
  else:
    return jsonify({'error': 'User not found'})

# Добавить нового пользователя в базу данных
@app.route('/users', methods=['POST'])
def add_user():
  data = request.get_json()
  name = data.get('name')
  if name:
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': 'User added'})
  else:
    return jsonify({'error': 'Missing data'})

# Удалить пользователя из базы данных по имени
@app.route('/users/<name>', methods=['DELETE'])
def delete_user(name):
  user = User.query.filter_by(name=name).first()
  if user:
    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': 'User deleted'})
  else:
    return jsonify({'error': 'User not found'})

# Получить список всех отзывов о книге по названию
@app.route('/reviews/<title>', methods=['GET'])
def get_reviews(title):
  book = Book.query.filter_by(title=title).first()
  if book:
    reviews = Review.query.filter_by(book_id=book.id).all()
    return jsonify([{
      'user': User.query.get(review.user_id).name,
      'rating': review.rating,
      'comment': review.comment
    } for review in reviews])
  else:
    return jsonify({'error': 'Book not found'})

# Добавить новый отзыв о книге в базу данных
@app.route('/reviews', methods=['POST'])
def add_review():
  data = request.get_json()
  user_name = data.get('user')
  book_title = data.get('book')
  rating = data.get('rating')
  comment = data.get('comment')
  if user_name and book_title and rating:
    user = User.query.filter_by(name=user_name).first()
    book = Book.query.filter_by(title=book_title).first()
    if user and book:
      review = Review(user_id=user.id, book_id=book.id, rating=rating, comment=comment)
      db.session.add(review)
      db.session.commit()
      return jsonify({'success': 'Review added'})
    else:
      return jsonify({'error': 'User or book not found'})
  else:
    return jsonify({'error': 'Missing data'})

# Запускаем приложение
if __name__ == '__main__':
  app.run(debug=True)
