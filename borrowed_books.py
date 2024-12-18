import db  # Assuming you have a `db.py` that manages the connection

def manage_borrowed_books():
    while True:
        print("\n1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrowed Books")
        print("4. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_borrowed_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def borrow_book():
    book_id = input("Enter the book ID to borrow: ")
    borrower_id = input("Enter the borrower ID: ")
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    
    # Check if the book exists and is not already borrowed
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()

    # Check if the book exists
    cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    
    if not book:
        print("The book does not exist.")
        cursor.close()
        connection.close()
        return
    
    # Check if the borrower exists
    cursor.execute("SELECT id FROM borrowers WHERE id = %s", (borrower_id,))
    borrower = cursor.fetchone()
    
    if not borrower:
        print("The borrower does not exist.")
        cursor.close()
        connection.close()
        return
    
    # Ensure the book is not already borrowed (assuming no return_date means it is borrowed)
    cursor.execute("SELECT * FROM borrowed_books WHERE book_id = %s AND return_date IS NULL", (book_id,))
    existing_borrow = cursor.fetchone()
    
    if existing_borrow:
        print(f"The book is already borrowed by someone else.")
        cursor.close()
        connection.close()
        return
    
    # Proceed with borrowing the book
    cursor.execute("INSERT INTO borrowed_books (book_id, borrower_id, borrow_date) VALUES (%s, %s, %s)", (book_id, borrower_id, borrow_date))
    connection.commit()
    print("Book borrowed successfully.")
    
    cursor.close()
    connection.close()

def return_book():
    borrowed_id = input("Enter the borrowed book ID to return: ")
    return_date = input("Enter return date (YYYY-MM-DD): ")
    
    # Ensure the borrowed book exists and has not already been returned
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM borrowed_books WHERE id = %s AND return_date IS NULL", (borrowed_id,))
    borrowed_book = cursor.fetchone()

    if not borrowed_book:
        print("This book has either not been borrowed or already returned.")
        cursor.close()
        connection.close()
        return
    
    # Ensure return date is not earlier than borrow date
    if return_date < borrowed_book[3]:
        print("Return date cannot be earlier than borrow date.")
        cursor.close()
        connection.close()
        return
    
    # Update return date
    cursor.execute("UPDATE borrowed_books SET return_date = %s WHERE id = %s", (return_date, borrowed_id))
    connection.commit()
    print("Book returned successfully.")
    
    cursor.close()
    connection.close()

def view_borrowed_books():
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()

    # Fetch all borrowed books along with book title and borrower name
    cursor.execute("""
        SELECT bb.id, b.title, br.name, bb.borrow_date, bb.return_date
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        JOIN borrowers br ON bb.borrower_id = br.id
    """)
    borrowed_books = cursor.fetchall()
    
    if borrowed_books:
        print("\nList of Borrowed Books:")
        print(f"{'ID':<5} {'Book Title':<30} {'Borrower Name':<25} {'Borrow Date':<15} {'Return Date':<15}")
        for borrowed_book in borrowed_books:
            print(f"{borrowed_book[0]:<5} {borrowed_book[1]:<30} {borrowed_book[2]:<25} {borrowed_book[3]:<15} {borrowed_book[4]:<15}")
    else:
        print("No books have been borrowed yet.")
    
    cursor.close()
    connection.close()
