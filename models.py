from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Declare the base class for models
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', backref='books')

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    borrower_id = Column(Integer, ForeignKey('borrowers.id'))
    borrow_date = Column(Date)
    return_date = Column(Date)

    book = relationship('Book')
    borrower = relationship('Borrower')
