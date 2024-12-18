import books
import authors
import borrowers
import borrowed_books

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Manage Books")
        print("2. Manage Authors")
        print("3. Manage Borrowers")
        print("4. Manage Borrowed Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            books.manage_books()
        elif choice == "2":
            authors.manage_authors()
        elif choice == "3":
            borrowers.manage_borrowers()
        elif choice == "4":
            borrowed_books.manage_borrowed_books()
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
