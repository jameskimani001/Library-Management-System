from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Define the Base class for SQLAlchemy models
Base = declarative_base()

# SQLite connection setup
DATABASE_URL = 'sqlite:///library_management_system.db'  # SQLite database file

# SQLAlchemy Models for the Library Management System

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    
    books = relationship("Book", back_populates="author")
    
    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship("Author", back_populates="books")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author_id={self.author_id})>"

class Borrower(Base):
    __tablename__ = 'borrowers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    
    borrowed_books = relationship("BorrowedBook", back_populates="borrower")
    
    def __repr__(self):
        return f"<Borrower(id={self.id}, name={self.name}, email={self.email})>"

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    borrower_id = Column(Integer, ForeignKey('borrowers.id'))
    borrow_date = Column(Date)
    return_date = Column(Date)
    
    book = relationship("Book")
    borrower = relationship("Borrower", back_populates="borrowed_books")
    
    def __repr__(self):
        return f"<BorrowedBook(id={self.id}, book_id={self.book_id}, borrower_id={self.borrower_id}, borrow_date={self.borrow_date})>"

# Function to create tables in the SQLite database using SQLAlchemy
def create_tables():
    """Creates tables in the SQLite database if they don't already exist."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Will not recreate existing tables
    print("Tables created successfully.")

# Function to get SQLAlchemy session
def get_session():
    """Establish a session to interact with the database."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

# Helper function to validate date format
def validate_date_format(date_string):
    """Validates the date format (YYYY-MM-DD)."""
    try:
        # Attempt to parse the date in the expected format
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Function to add a book to the database
def add_book(title, author_id):
    """Adds a book to the database."""
    session = get_session()
    try:
        new_book = Book(title=title, author_id=author_id)
        session.add(new_book)
        session.commit()
        print("Book added successfully.")
    except IntegrityError:
        print(f"Error: Author with ID {author_id} does not exist.")
    finally:
        session.close()

# Function to view all books
def view_books():
    """Displays all books from the database."""
    session = get_session()
    books = session.query(Book).all()
    print("\n--- List of Books ---")
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}")
    session.close()

# Function to add an author to the database
def add_author(name):
    """Adds an author to the database."""
    session = get_session()
    new_author = Author(name=name)
    session.add(new_author)
    session.commit()
    print("Author added successfully.")
    session.close()

# Function to view all authors
def view_authors():
    """Displays all authors from the database."""
    session = get_session()
    authors = session.query(Author).all()
    print("\n--- List of Authors ---")
    for author in authors:
        print(f"ID: {author.id}, Name: {author.name}")
    session.close()

# Function to add a borrower to the database
def add_borrower(name, email, phone):
    """Adds a borrower to the database."""
    session = get_session()
    new_borrower = Borrower(name=name, email=email, phone=phone)
    session.add(new_borrower)
    session.commit()
    print("Borrower added successfully.")
    session.close()

# Function to view all borrowers
def view_borrowers():
    """Displays all borrowers from the database."""
    session = get_session()
    borrowers = session.query(Borrower).all()
    print("\n--- List of Borrowers ---")
    for borrower in borrowers:
        print(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}, Phone: {borrower.phone}")
    session.close()

# Function to borrow a book
def borrow_book(book_id, borrower_id, borrow_date, return_date):
    """Adds a borrowed book record to the database."""
    session = get_session()
    try:
        borrow_date = validate_date_format(borrow_date)
        return_date = validate_date_format(return_date)

        if return_date <= borrow_date:
            print("Error: The return date must be after the borrow date.")
            return
        
        new_borrowed_book = BorrowedBook(book_id=book_id, borrower_id=borrower_id, borrow_date=borrow_date, return_date=return_date)
        session.add(new_borrowed_book)
        session.commit()
        print("Book borrowed successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    except IntegrityError:
        print("Error: Invalid book or borrower ID.")
    finally:
        session.close()

# Function to view borrowed books
def view_borrowed_books():
    """Displays all borrowed books from the database."""
    session = get_session()
    borrowed_books = session.query(BorrowedBook).all()
    print("\n--- List of Borrowed Books ---")
    for borrowed_book in borrowed_books:
        print(f"ID: {borrowed_book.id}, Book ID: {borrowed_book.book_id}, Borrower ID: {borrowed_book.borrower_id}, Borrow Date: {borrowed_book.borrow_date}, Return Date: {borrowed_book.return_date}")
    session.close()

# Main function
def main():
    """Main menu for interacting with the library system."""
    while True:
        print("\n--- Library Management System ---")
        print("1. Manage Books")
        print("2. Manage Authors")
        print("3. Manage Borrowers")
        print("4. View Borrowed Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                print("\n--- Manage Books ---")
                print("1. Add Book")
                print("2. View Books")
                print("3. Go Back")
                
                book_choice = input("Enter your choice: ")
                
                if book_choice == "1":
                    title = input("Enter book title: ")
                    try:
                        author_id = int(input("Enter author ID: "))
                        add_book(title, author_id)
                    except ValueError:
                        print("Invalid input. Please enter a valid author ID (integer).")
                elif book_choice == "2":
                    view_books()
                elif book_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            while True:
                print("\n--- Manage Authors ---")
                print("1. Add Author")
                print("2. View Authors")
                print("3. Go Back")
                
                author_choice = input("Enter your choice: ")
                
                if author_choice == "1":
                    name = input("Enter author name: ")
                    add_author(name)
                elif author_choice == "2":
                    view_authors()
                elif author_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print("\n--- Manage Borrowers ---")
                print("1. Add Borrower")
                print("2. View Borrowers")
                print("3. Go Back")
                
                borrower_choice = input("Enter your choice: ")
                
                if borrower_choice == "1":
                    name = input("Enter borrower name: ")
                    email = input("Enter borrower email: ")
                    phone = input("Enter borrower phone number: ")
                    add_borrower(name, email, phone)
                elif borrower_choice == "2":
                    view_borrowers()
                elif borrower_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                print("\n--- Manage Borrowed Books ---")
                print("1. Borrow Book")
                print("2. View Borrowed Books")
                print("3. Go Back")
                
                borrowed_choice = input("Enter your choice: ")
                
                if borrowed_choice == "1":
                    try:
                        book_id = int(input("Enter book ID: "))
                        borrower_id = int(input("Enter borrower ID: "))
                        borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
                        return_date = input("Enter return date (YYYY-MM-DD): ")
                        borrow_book(book_id, borrower_id, borrow_date, return_date)
                    except ValueError:
                        print("Invalid input. Please enter valid IDs and dates.")
                elif borrowed_choice == "2":
                    view_borrowed_books()
                elif borrowed_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create tables in the SQLite database if not already created
    create_tables()

    # Run the main menu for the library system
    main()
