import db  # Assuming you have a `db.py` that manages the connection

def manage_authors():
    while True:
        print("\n1. Add Author")
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
    name = input("Enter author name: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("INSERT INTO authors (name) VALUES (%s)", (name,))
    connection.commit()
    print("Author added successfully.")
    cursor.close()
    connection.close()

def view_authors():
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    for author in authors:
        print(f"ID: {author[0]}, Name: {author[1]}")
    cursor.close()
    connection.close()

def update_author():
    author_id = input("Enter the author ID to update: ")
    new_name = input("Enter new author name: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("UPDATE authors SET name = %s WHERE id = %s", (new_name, author_id))
    connection.commit()
    print("Author updated successfully.")
    cursor.close()
    connection.close()

def delete_author():
    author_id = input("Enter the author ID to delete: ")
    
    connection = db.get_connection()  # Using db.py for connection handling
    cursor = connection.cursor()
    cursor.execute("DELETE FROM authors WHERE id = %s", (author_id,))
    connection.commit()
    print("Author deleted successfully.")
    cursor.close()
    connection.close()
