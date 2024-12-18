import mysql.connector

def get_connection():
    """Establish and return a connection to the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',  # Your MySQL password
            database='LibraryManagementSystem'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def check_author_exists(author_id):
    """Check if an author exists in the authors table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT id FROM authors WHERE id = %s"
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
        return

    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO books (title, author_id) VALUES (%s, %s)"
            cursor.execute(query, (title, author_id))
            connection.commit()
            print("Book added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

def view_books():
    """View all books in the books table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        if books:
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
            query = "UPDATE books SET title = %s WHERE id = %s"
            cursor.execute(query, (new_title, book_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Book updated successfully!")
            else:
                print("No book found with that ID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

def delete_book(book_id):
    """Delete a book from the books table."""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Book deleted successfully!")
            else:
                print("No book found with that ID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

# Example usage:
# add_book("The River and the Source", 3)
# view_books()
# update_book(1, "The River and the Source - Updated")
# delete_book(1)
