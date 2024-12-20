import sqlite3

def create_tables():
    """Create tables for the library management system using SQLite."""
    connection = None  # Initialize connection variable outside the try block
    cursor = None  # Initialize cursor variable outside the try block
    
    try:
        # Establish the connection to SQLite database
        connection = sqlite3.connect('library_management_system.db')  # SQLite database file
        cursor = connection.cursor()
        print("Successfully connected to the SQLite database.")

        # Create authors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        print("Authors table created.")

        # Create books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            );
        """)
        print("Books table created.")

        # Create borrowers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        print("Borrowers table created.")

        # Create borrowed_books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowed_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                borrower_id INTEGER,
                borrow_date TEXT,
                return_date TEXT,
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
            );
        """)
        print("Borrowed Books table created.")
    
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensure that cursor and connection are properly closed if they were created
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if connection:
            connection.close()
            print("Connection closed.")

# Run the function to create tables
create_tables()
