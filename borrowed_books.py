import sqlite3
from db import get_connection
from datetime import datetime

def manage_borrowed_books():
    while True:
        print("\n--- Manage Borrowed Books ---")
        print("1. Borrow a Book")
        print("2. View Borrowed Books")
        print("3. Return a Book")
        print("4. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            borrow_book()
        elif choice == "2":
            view_borrowed_books()
        elif choice == "3":
            return_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def borrow_book():
    try:
        book_id = int(input("Enter book ID to borrow: "))
        borrower_id = int(input("Enter borrower ID: "))

        # Check if book exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        
        if book is None:
            print(f"No book found with ID {book_id}. Please check the ID and try again.")
            return

        cursor.execute("SELECT id FROM borrowers WHERE id = ?", (borrower_id,))
        borrower = cursor.fetchone()

        if borrower is None:
            print(f"No borrower found with ID {borrower_id}. Please check the ID and try again.")
            return

        # Check if the book is already borrowed
        cursor.execute("SELECT id FROM borrowed_books WHERE book_id = ? AND return_date IS NULL", (book_id,))
        existing_borrow = cursor.fetchone()
        
        if existing_borrow:
            print(f"The book with ID {book_id} is already borrowed and not yet returned.")
            return

        # Set borrow date to today by default
        borrow_date = datetime.today().date()

        return_date = input("Enter return date (YYYY-MM-DD): ")

        # Validate date format
        try:
            return_date = validate_date_format(return_date)
        except ValueError as e:
            print(e)
            return
        
        # Insert the borrowed book into the database
        cursor.execute("INSERT INTO borrowed_books (book_id, borrower_id, borrow_date, return_date) VALUES (?, ?, ?, ?)",
                       (book_id, borrower_id, borrow_date, return_date))
        connection.commit()

        print("Book borrowed successfully!")
    except ValueError:
        print("Invalid input. Please enter valid numeric IDs for book and borrower.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def view_borrowed_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT borrowed_books.id, books.title, borrowers.name, borrow_date, return_date "
                   "FROM borrowed_books "
                   "JOIN books ON borrowed_books.book_id = books.id "
                   "JOIN borrowers ON borrowed_books.borrower_id = borrowers.id")
    borrowed_books = cursor.fetchall()
    
    print("\n--- List of Borrowed Books ---")
    if borrowed_books:
        for record in borrowed_books:
            print(f"ID: {record[0]}, Book: {record[1]}, Borrower: {record[2]}, Borrow Date: {record[3]}, Return Date: {record[4]}")
    else:
        print("No borrowed books found.")
    connection.close()

def return_book():
    try:
        borrowed_book_id = int(input("Enter borrowed book ID to return: "))
        
        # Check if borrowed book exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM borrowed_books WHERE id = ?", (borrowed_book_id,))
        borrowed_book = cursor.fetchone()

        if borrowed_book is None:
            print(f"No borrowed book found with ID {borrowed_book_id}. Please check the ID and try again.")
            return

        # Mark the book as returned by updating the return_date
        return_date = datetime.today().date()  # Set today's date as the return date
        cursor.execute("UPDATE borrowed_books SET return_date = ? WHERE id = ?", (return_date, borrowed_book_id))
        connection.commit()

        print("Book returned successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric borrowed book ID.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# Helper function to validate date format
def validate_date_format(date_string):
    """Validates the date format (YYYY-MM-DD)."""
    try:
        # Attempt to parse the date in the expected format
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")
