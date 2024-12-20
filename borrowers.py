import sqlite3
from db import get_connection

def manage_borrowers():
    while True:
        print("\n--- Manage Borrowers ---")
        print("1. Add Borrower")
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
    name = input("Enter borrower name: ").strip()
    
    if not name:
        print("Borrower name cannot be empty.")
        return
    
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO borrowers (name) VALUES (?)", (name,))
        connection.commit()
        print("Borrower added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding borrower: {e}")
    finally:
        connection.close()

def view_borrowers():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM borrowers")
    borrowers = cursor.fetchall()
    
    print("\n--- List of Borrowers ---")
    if borrowers:
        for borrower in borrowers:
            print(f"ID: {borrower[0]}, Name: {borrower[1]}")
    else:
        print("No borrowers found.")
    
    connection.close()

def update_borrower():
    try:
        borrower_id = int(input("Enter borrower ID to update: "))
        new_name = input("Enter new borrower name: ").strip()

        if not new_name:
            print("Borrower name cannot be empty.")
            return
        
        connection = get_connection()
        cursor = connection.cursor()
        
        # Check if borrower exists
        cursor.execute("SELECT id, name FROM borrowers WHERE id = ?", (borrower_id,))
        borrower = cursor.fetchone()

        if borrower is None:
            print(f"No borrower found with ID {borrower_id}. Please check the ID and try again.")
            connection.close()
            return
        
        # Check if the new name is different from the old one
        if new_name == borrower[1]:
            print("New name is the same as the current name. No update necessary.")
            connection.close()
            return

        cursor.execute("UPDATE borrowers SET name = ? WHERE id = ?", (new_name, borrower_id))
        connection.commit()
        print("Borrower updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric borrower ID.")
    except sqlite3.Error as e:
        print(f"Error updating borrower: {e}")
    finally:
        connection.close()

def delete_borrower():
    try:
        borrower_id = int(input("Enter borrower ID to delete: "))
        
        connection = get_connection()
        cursor = connection.cursor()
        
        # Check if the borrower exists
        cursor.execute("SELECT id FROM borrowers WHERE id = ?", (borrower_id,))
        borrower = cursor.fetchone()

        if borrower is None:
            print(f"No borrower found with ID {borrower_id}. Please check the ID and try again.")
            connection.close()
            return
        
        # Check if the borrower has any borrowed books
        cursor.execute("SELECT id FROM borrowed_books WHERE borrower_id = ?", (borrower_id,))
        borrowed_books = cursor.fetchall()

        if borrowed_books:
            print(f"Cannot delete borrower with ID {borrower_id} because they have borrowed books.")
            connection.close()
            return

        cursor.execute("DELETE FROM borrowers WHERE id = ?", (borrower_id,))
        connection.commit()
        print("Borrower deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric borrower ID.")
    except sqlite3.Error as e:
        print(f"Error deleting borrower: {e}")
    finally:
        connection.close()
