import mysql.connector
from mysql.connector import Error

def create_tables():
    """Create tables for the library management system."""
    connection = None  # Initialize connection variable outside the try block
    cursor = None  # Initialize cursor variable outside the try block
    
    try:
        # Establish the connection without using a password
        connection = mysql.connector.connect(
            host='localhost',
            database='LibraryManagementSystem',  # Specify the database here
            user='root'  # No password needed as MySQL is configured to skip authentication
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print("Successfully connected to the database.")

            # Create authors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                );
            """)
            print("Authors table created.")

            # Create books table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author_id INT,
                    FOREIGN KEY (author_id) REFERENCES authors(id)
                );
            """)
            print("Books table created.")

            # Create borrowers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS borrowers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                );
            """)
            print("Borrowers table created.")

            # Create borrowed_books table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS borrowed_books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    book_id INT,
                    borrower_id INT,
                    borrow_date DATE,
                    return_date DATE,
                    FOREIGN KEY (book_id) REFERENCES books(id),
                    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
                );
            """)
            print("Borrowed Books table created.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensure that cursor and connection are properly closed if they were created
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

# Run the function to create tables
create_tables()
