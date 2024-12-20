import sqlite3
from db import get_connection

def manage_authors():
    while True:
        print("\n--- Manage Authors ---")
        print("1. Add Author")
        print("2. View Authors")
        print("3. Update Author")
        print("4. Delete Author")
        print("5. Go Back")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_author()
        elif choice == "2":
            view_authors()
        elif choice == "3":
            update_author()
        elif choice == "4":
            delete_author()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_author():
    name = input("Enter author name: ").strip()
    if not name:
        print("Author name cannot be empty.")
        return
    
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        connection.commit()
        print("Author added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding author: {e}")
    finally:
        connection.close()

def view_authors():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    
    print("\n--- List of Authors ---")
    if authors:
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}")
    else:
        print("No authors found.")
    
    connection.close()

def update_author():
    try:
        author_id = int(input("Enter author ID to update: "))
        new_name = input("Enter new author name: ").strip()

        if not new_name:
            print("Author name cannot be empty.")
            return
        
        connection = get_connection()
        cursor = connection.cursor()

        # Check if the author exists
        cursor.execute("SELECT id, name FROM authors WHERE id = ?", (author_id,))
        author = cursor.fetchone()

        if author is None:
            print(f"No author found with ID {author_id}. Please check the ID and try again.")
            connection.close()
            return
        
        # Check if the new name is different from the old name
        if new_name == author[1]:
            print("New name is the same as the current name. No update necessary.")
            connection.close()
            return

        cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (new_name, author_id))
        connection.commit()
        print("Author updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric author ID.")
    except sqlite3.Error as e:
        print(f"Error updating author: {e}")
    finally:
        connection.close()

def delete_author():
    try:
        author_id = int(input("Enter author ID to delete: "))
        
        connection = get_connection()
        cursor = connection.cursor()

        # Check if the author exists
        cursor.execute("SELECT id FROM authors WHERE id = ?", (author_id,))
        author = cursor.fetchone()

        if author is None:
            print(f"No author found with ID {author_id}. Please check the ID and try again.")
            connection.close()
            return
        
        # Check if the author is linked to any books
        cursor.execute("SELECT id FROM books WHERE author_id = ?", (author_id,))
        books = cursor.fetchall()
        
        if books:
            print(f"The author with ID {author_id} is linked to one or more books. Cannot delete.")
            connection.close()
            return
        
        cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        connection.commit()
        print("Author deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric author ID.")
    except sqlite3.Error as e:
        print(f"Error deleting author: {e}")
    finally:
        connection.close()
