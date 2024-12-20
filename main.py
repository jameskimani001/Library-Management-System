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

# Function to validate date format
def validate_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None

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

# Function to update a book in the database
def update_book(book_id, new_title, new_author_id):
    """Updates a book's title and author in the database."""
    session = get_session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = new_title
        book.author_id = new_author_id
        session.commit()
        print("Book updated successfully.")
    else:
        print(f"No book found with ID {book_id}.")
    session.close()

# Function to delete a book from the database
def delete_book(book_id):
    """Deletes a book from the database."""
    session = get_session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully.")
    else:
        print(f"No book found with ID {book_id}.")
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

# Function to update an author in the database
def update_author(author_id, new_name):
    """Updates an author's name in the database."""
    session = get_session()
    author = session.query(Author).filter(Author.id == author_id).first()
    if author:
        author.name = new_name
        session.commit()
        print("Author updated successfully.")
    else:
        print(f"No author found with ID {author_id}.")
    session.close()

# Function to delete an author from the database
def delete_author(author_id):
    """Deletes an author from the database."""
    session = get_session()
    author = session.query(Author).filter(Author.id == author_id).first()
    if author:
        session.delete(author)
        session.commit()
        print("Author deleted successfully.")
    else:
        print(f"No author found with ID {author_id}.")
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

# Function to update a borrower
def update_borrower(borrower_id, new_name, new_email, new_phone):
    """Updates borrower's details in the database."""
    session = get_session()
    borrower = session.query(Borrower).filter(Borrower.id == borrower_id).first()
    if borrower:
        borrower.name = new_name
        borrower.email = new_email
        borrower.phone = new_phone
        session.commit()
        print("Borrower updated successfully.")
    else:
        print(f"No borrower found with ID {borrower_id}.")
    session.close()

# Function to delete a borrower
def delete_borrower(borrower_id):
    """Deletes a borrower from the database."""
    session = get_session()
    borrower = session.query(Borrower).filter(Borrower.id == borrower_id).first()
    if borrower:
        session.delete(borrower)
        session.commit()
        print("Borrower deleted successfully.")
    else:
        print(f"No borrower found with ID {borrower_id}.")
    session.close()

# Function to borrow a book with date validation and duplicate check
def borrow_book(book_id, borrower_id, borrow_date, return_date):
    """Adds a borrowed book record to the database."""
    session = get_session()
    
    # Validate date format
    borrow_date = validate_date(borrow_date)
    return_date = validate_date(return_date)
    
    if not borrow_date or not return_date:
        print("Invalid date format. Please use YYYY-MM-DD.")
        session.close()
        return
    
    if return_date <= borrow_date:
        print("Return date cannot be earlier than or equal to borrow date.")
        session.close()
        return
    
    # Check if the book is already borrowed (pending return)
    existing_borrow = session.query(BorrowedBook).filter(BorrowedBook.book_id == book_id, BorrowedBook.return_date == None).first()
    if existing_borrow:
        print(f"The book with ID {book_id} is already borrowed and not yet returned.")
        session.close()
        return
    
    new_borrowed_book = BorrowedBook(book_id=book_id, borrower_id=borrower_id, borrow_date=borrow_date, return_date=return_date)
    try:
        session.add(new_borrowed_book)
        session.commit()
        print("Book borrowed successfully.")
    except IntegrityError as e:
        print(f"Error: {e}")
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

# Function to update borrowed book return date
def update_borrowed_book(borrowed_book_id, new_return_date):
    """Updates the return date for a borrowed book."""
    session = get_session()
    
    # Validate the new return date
    new_return_date = validate_date(new_return_date)
    if not new_return_date:
        print("Invalid date format. Please use YYYY-MM-DD.")
        session.close()
        return
    
    borrowed_book = session.query(BorrowedBook).filter(BorrowedBook.id == borrowed_book_id).first()
    if borrowed_book:
        borrowed_book.return_date = new_return_date
        session.commit()
        print("Borrowed book return date updated successfully.")
    else:
        print(f"No borrowed book found with ID {borrowed_book_id}.")
    session.close()

# Function to delete a borrowed book entry
def delete_borrowed_book(borrowed_book_id):
    """Deletes a borrowed book from the database."""
    session = get_session()
    borrowed_book = session.query(BorrowedBook).filter(BorrowedBook.id == borrowed_book_id).first()
    if borrowed_book:
        session.delete(borrowed_book)
        session.commit()
        print("Borrowed book deleted successfully.")
    else:
        print(f"No borrowed book found with ID {borrowed_book_id}.")
    session.close()

# Function to manage borrowed books with CRUD options
def manage_borrowed_books():
    """Menu to manage borrowed books."""
    while True:
        print("\n--- Manage Borrowed Books ---")
        print("1. Borrow Book")
        print("2. View Borrowed Books")
        print("3. Update Borrowed Book Return Date")
        print("4. Delete Borrowed Book")
        print("5. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_id = int(input("Enter book ID to borrow: "))
            borrower_id = int(input("Enter borrower ID: "))
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            return_date = input("Enter return date (YYYY-MM-DD): ")
            borrow_book(book_id, borrower_id, borrow_date, return_date)
        elif choice == "2":
            view_borrowed_books()
        elif choice == "3":
            borrowed_book_id = int(input("Enter borrowed book ID to update: "))
            new_return_date = input("Enter new return date (YYYY-MM-DD): ")
            update_borrowed_book(borrowed_book_id, new_return_date)
        elif choice == "4":
            borrowed_book_id = int(input("Enter borrowed book ID to delete: "))
            delete_borrowed_book(borrowed_book_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Main function with options for managing books, authors, borrowers, and borrowed books
def main():
    """Main menu for interacting with the library system."""
    while True:
        print("\n--- Library Management System ---")
        print("1. Manage Books")
        print("2. Manage Authors")
        print("3. Manage Borrowers")
        print("4. Manage Borrowed Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                print("\n--- Manage Books ---")
                print("1. Add Book")
                print("2. View Books")
                print("3. Update Book")
                print("4. Delete Book")
                print("5. Go Back")
                book_choice = input("Enter your choice: ")
                
                if book_choice == "1":
                    title = input("Enter book title: ")
                    author_id = int(input("Enter author ID: "))
                    add_book(title, author_id)
                elif book_choice == "2":
                    view_books()
                elif book_choice == "3":
                    book_id = int(input("Enter book ID to update: "))
                    new_title = input("Enter new title: ")
                    new_author_id = int(input("Enter new author ID: "))
                    update_book(book_id, new_title, new_author_id)
                elif book_choice == "4":
                    book_id = int(input("Enter book ID to delete: "))
                    delete_book(book_id)
                elif book_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            while True:
                print("\n--- Manage Authors ---")
                print("1. Add Author")
                print("2. View Authors")
                print("3. Update Author")
                print("4. Delete Author")
                print("5. Go Back")
                author_choice = input("Enter your choice: ")
                
                if author_choice == "1":
                    name = input("Enter author name: ")
                    add_author(name)
                elif author_choice == "2":
                    view_authors()
                elif author_choice == "3":
                    author_id = int(input("Enter author ID to update: "))
                    new_name = input("Enter new author name: ")
                    update_author(author_id, new_name)
                elif author_choice == "4":
                    author_id = int(input("Enter author ID to delete: "))
                    delete_author(author_id)
                elif author_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "3":
            while True:
                print("\n--- Manage Borrowers ---")
                print("1. Add Borrower")
                print("2. View Borrowers")
                print("3. Update Borrower")
                print("4. Delete Borrower")
                print("5. Go Back")
                borrower_choice = input("Enter your choice: ")
                
                if borrower_choice == "1":
                    name = input("Enter borrower name: ")
                    email = input("Enter borrower email: ")
                    phone = input("Enter borrower phone: ")
                    add_borrower(name, email, phone)
                elif borrower_choice == "2":
                    view_borrowers()
                elif borrower_choice == "3":
                    borrower_id = int(input("Enter borrower ID to update: "))
                    new_name = input("Enter new name: ")
                    new_email = input("Enter new email: ")
                    new_phone = input("Enter new phone: ")
                    update_borrower(borrower_id, new_name, new_email, new_phone)
                elif borrower_choice == "4":
                    borrower_id = int(input("Enter borrower ID to delete: "))
                    delete_borrower(borrower_id)
                elif borrower_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "4":
            manage_borrowed_books()
        
        elif choice == "5":
            print("Exiting Library Management System...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Initialize the database and create tables
create_tables()

# Start the application
main()
