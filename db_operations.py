import sqlite3

def get_connection():
    """Establish and return a connection to the SQLite database."""
    try:
        connection = sqlite3.connect('library_management_system.db')  # Path to SQLite database file
        print("Successfully connected to the database.")
        return connection
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None

def check_author_exists(author_id):
    """Check if an author exists in the authors table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT id FROM authors WHERE id = ?"
        print(f"Executing query: {query} with author_id={author_id}")
        cursor.execute(query, (author_id,))
        author_exists = cursor.fetchone()
        cursor.close()
        connection.close()
        return author_exists is not None
    else:
        print("Failed to connect to the database.")
        return False

def add_book(title, author_id):
    """Add a new book to the books table."""
    if not check_author_exists(author_id):
        print(f"Error: No author found with ID {author_id}. Please add the author first.")
        return False  # Indicate failure
    
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO books (title, author_id) VALUES (?, ?)"
            cursor.execute(query, (title, author_id))
            connection.commit()
            print("Book added successfully!")
            return True  # Indicate success
        except sqlite3.Error as err:
            print(f"Error: {err}")
            return False  # Indicate failure
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")
        return False  # Indicate failure

def view_books():
    """View all books in the books table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT id, title, author_id FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        if books:
            print("\n--- List of Books ---")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}")
        else:
            print("No books found.")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def update_book(book_id, new_title):
    """Update the title of a book in the books table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "UPDATE books SET title = ? WHERE id = ?"
            cursor.execute(query, (new_title, book_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Book updated successfully!")
                return True  # Indicate success
            else:
                print("No book found with that ID.")
                return False  # Indicate failure
        except sqlite3.Error as err:
            print(f"Error: {err}")
            return False  # Indicate failure
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")
        return False  # Indicate failure

def delete_book(book_id):
    """Delete a book from the books table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM books WHERE id = ?"
            cursor.execute(query, (book_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Book deleted successfully!")
                return True  # Indicate success
            else:
                print("No book found with that ID.")
                return False  # Indicate failure
        except sqlite3.Error as err:
            print(f"Error: {err}")
            return False  # Indicate failure
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")
        return False  # Indicate failure


# Example usage:
# add_book("The River and the Source", 3)
# view_books()
# update_book(1, "The River and the Source - Updated")
# delete_book(1)
