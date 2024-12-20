import sqlite3
from db import get_connection

def manage_books():
    while True:
        print("\n--- Manage Books ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter book title: ")
    
    # Ensure the author ID is valid
    try:
        author_id = int(input("Enter author ID: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric author ID.")
        return
    
    # Check if author exists
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id FROM authors WHERE id = ?", (author_id,))
        author = cursor.fetchone()

        if author is None:
            print(f"No author found with ID {author_id}. Please add the author first.")
            return

        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
        connection.commit()
        print("Book added successfully!")

    except sqlite3.Error as e:
        print(f"Error adding book: {e}")
    finally:
        connection.close()

def view_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT books.id, books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id")
    books = cursor.fetchall()
    
    print("\n--- List of Books ---")
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    else:
        print("No books found.")
    
    connection.close()

def update_book():
    try:
        book_id = int(input("Enter book ID to update: "))
        
        # Check if the book exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()

        if book is None:
            print(f"No book found with ID {book_id}. Please check the ID and try again.")
            return

        # Proceed with updating the book title
        new_title = input("Enter new title: ")

        cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
        connection.commit()
        print("Book updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid numeric book ID.")
    except sqlite3.Error as e:
        print(f"Error updating book: {e}")
    finally:
        connection.close()

def delete_book():
    try:
        book_id = int(input("Enter book ID to delete: "))

        # Check if the book exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()

        if book is None:
            print(f"No book found with ID {book_id}. Please check the ID and try again.")
            return

        # Delete the book
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        print("Book deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid num3eric book ID.")
    except sqlite3.Error as e:
        print(f"Error deleting book: {e}")
    finally:
        connection.close()
