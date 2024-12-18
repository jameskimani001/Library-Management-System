## name JAMES KIMANI
## DATE 17-12-2024
## Library Management System
A Python-based Library Management System that allows the management of books, authors, borrowers, and borrowed books. The system interacts with a MySQL database to store and manage data, and provides an interactive command-line interface (CLI) for performing operations.

## Features
Manage Books: Add, view, update, and delete books in the library.
Manage Authors: Add, view, update, and delete authors.
Manage Borrowers: Add, view, update, and delete borrowers.
Manage Borrowed Books: Borrow and return books, view borrowed books.
## Prerequisites
Before using the system, ensure that you have the following installed:

Python 3.x
MySQL (version 5.7 or higher recommended)
MySQL Connector for Python (mysql-connector-python)
Installation Steps
# Install MySQL Server
Install MySQL on your system (if not already installed).

On Ubuntu/Debian-based systems:
sudo apt update
sudo apt install mysql-server
## After installation, start the MySQL service:
sudo systemctl start mysql
## Secure MySQL installation:
sudo mysql_secure_installation
Set a password for the MySQL root user when prompted.

# Install Python and Dependencies
Ensure that Python 3.x is installed on your machine. To install Python 3.x:
Copy code
sudo apt install python3 python3-pip
Next, create a virtual environment and install the required dependencies:
Copy code
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the required libraries
pip install mysql-connector-python
# Create the Database
Log into MySQL using the following command:
Copy code
sudo mysql -u root -p
## Once logged in, create the database and tables required for the project:
sql
CREATE DATABASE LibraryManagementSystem;

USE LibraryManagementSystem;

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE borrowers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    borrower_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
);
# Configure MySQL Connection
Make sure to update the MySQL connection details in the create_tables.py file if necessary. By default, the connection settings should be:
def get_connection():
    """Establish and return a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host='localhost',
        database='LibraryManagementSystem',  # Specify your database here
        user='root',  # MySQL root user
        password='1234'  # Update with your password
    )
    return connection
# Run the Application
To run the application, simply execute the main.py file. This will launch an interactive CLI for managing the library.
python3 main.py
# Usage
Once the program starts, you'll see a menu with the following options:

markdown
Copy code
1. Manage Books
2. Manage Authors
3. Manage Borrowers
4. Manage Borrowed Books
5. Exit
## Select an option to manage the corresponding entity. For example:

## Manage Books:

Add a new book by providing the title and author ID.
View all books in the library.
Update a book's title.
Delete a book from the library.

## Manage Authors:

Add a new author.
View all authors.
Update an author's name.
Delete an author.

## Manage Borrowers:

Add a new borrower.
View all borrowers.
Update a borrower's details.
Delete a borrower.

## Manage Borrowed Books:

Borrow a book by providing the book ID and borrower ID.
Return a borrowed book.
View all borrowed books with borrow and return dates.
To exit the system, simply select the "Exit" option.

## Example Usage
Adding a New Book:
Choose "Manage Books".
Choose "Add Book".
Enter the book title (e.g., "The Great Gatsby").
Enter the author ID (e.g., "1").
Viewing Books:
Choose "Manage Books".
Choose "View Books".
Borrowing a Book:
Choose "Manage Borrowed Books".
Choose "Borrow Book".
Enter the book ID and borrower ID.
Enter the borrow date.
# Error Handling
If the application cannot connect to the MySQL database, ensure that:

MySQL is running.
The database and tables are correctly created.
The MySQL user and password in the code are correct.
You can start MySQL using:
sudo systemctl start mysql
## If MySQL doesn't start, check its status with:
sudo systemctl status mysql
# Contributing
Feel free to contribute to this project by forking the repository and submitting pull requests. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Submit a pull request.
## . License
This project is licensed under the MIT License - see the LICENSE file for details.
# access command line 
mysql -u root -p
## codded with passion and love by techie kim