from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

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