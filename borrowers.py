import db  # Assuming you have a `db.py` that manages the connection

def manage_borrowers():
    while True:
        print("\n1. Add Borrower")
        print("2. View Borrowers")
        print("3. Update Borrower")
        print("4. Delete Borrower")
        print("5. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_borrower()
        elif choice == "2":
            view_borrowers()
        elif choice == "3":
            update_borrower()
        elif choice == "4":
            delete_borrower()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_borrower():
    name = input("Enter borrower name: ")
    email = input("Enter borrower email: ")
    phone = input("Enter borrower phone number: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    
    # Insert data into the borrowers table (assuming it has name, email, and phone fields)
    cursor.execute("INSERT INTO borrowers (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    connection.commit()
    print("Borrower added successfully.")
    cursor.close()
    connection.close()

def view_borrowers():
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    
    # Fetch all borrowers from the borrowers table
    cursor.execute("SELECT * FROM borrowers")
    borrowers = cursor.fetchall()
    
    if borrowers:
        print("\nList of Borrowers:")
        print(f"{'ID':<5} {'Name':<25} {'Email':<30} {'Phone':<15}")
        for borrower in borrowers:
            print(f"{borrower[0]:<5} {borrower[1]:<25} {borrower[2]:<30} {borrower[3]:<15}")
    else:
        print("No borrowers found.")
    
    cursor.close()
    connection.close()

def update_borrower():
    borrower_id = input("Enter the borrower ID to update: ")
    new_name = input("Enter new borrower name: ")
    new_email = input("Enter new borrower email: ")
    new_phone = input("Enter new borrower phone number: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    
    # Check if borrower exists
    cursor.execute("SELECT * FROM borrowers WHERE id = %s", (borrower_id,))
    borrower = cursor.fetchone()
    
    if borrower:
        # Update the borrower details
        cursor.execute("UPDATE borrowers SET name = %s, email = %s, phone = %s WHERE id = %s", 
                       (new_name, new_email, new_phone, borrower_id))
        connection.commit()
        print("Borrower updated successfully.")
    else:
        print(f"No borrower found with ID {borrower_id}.")
    
    cursor.close()
    connection.close()

def delete_borrower():
    borrower_id = input("Enter the borrower ID to delete: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    
    # Check if borrower exists
    cursor.execute("SELECT * FROM borrowers WHERE id = %s", (borrower_id,))
    borrower = cursor.fetchone()
    
    if borrower:
        # Delete the borrower
        cursor.execute("DELETE FROM borrowers WHERE id = %s", (borrower_id,))
        connection.commit()
        print("Borrower deleted successfully.")
    else:
        print(f"No borrower found with ID {borrower_id}.")
    
    cursor.close()
    connection.close()
