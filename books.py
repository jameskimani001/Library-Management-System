import db  # Assuming you have a `db.py` that manages the connection

def manage_books():
    while True:
        print("\n1. Add Book")
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
    author_id = input("Enter author ID: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author_id) VALUES (%s, %s)", (title, author_id))
    connection.commit()
    print("Book added successfully.")
    cursor.close()
    connection.close()

def view_books():
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}")
    cursor.close()
    connection.close()

def update_book():
    book_id = input("Enter the book ID to update: ")
    new_title = input("Enter new book title: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title = %s WHERE id = %s", (new_title, book_id))
    connection.commit()
    print("Book updated successfully.")
    cursor.close()
    connection.close()

def delete_book():
    book_id = input("Enter the book ID to delete: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    connection.commit()
    print("Book deleted successfully.")
    cursor.close()
    connection.close()
