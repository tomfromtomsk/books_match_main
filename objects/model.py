# from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, Date, Text
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  user_id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)

class Book(Base):
  __tablename__ = 'books'

  book_id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  author = Column(String(255), nullable=False)
  genre = Column(String(255), nullable=True)
  description = Column(String(255), nullable=True)
  year = Column(Integer, nullable=True)

  def __repr__(self):
    return f'<Book {self.title}>'

class Meeting(Base):
  __tablename__ = 'meetings'

  meeting_id = Column(Integer, primary_key=True)
  book_id = Column(Integer, nullable=False)
  user_id = Column(Integer, nullable=False)
  rating = Column(Integer, nullable=True)
  comment = Column(Text, nullable=True)
  date = Column(Date, nullable=True)
