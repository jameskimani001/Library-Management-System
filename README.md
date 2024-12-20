Library Management System
Author: James Kimani
Date: 17-12-2024

## Overview
The Library Management System is a Python-based application designed to help manage books, authors, borrowers, and borrowed books. It integrates with a MySQL database to store data and provides an interactive command-line interface (CLI) for performing various library operations.

## Features
Manage Books: Add, view, update, and delete books in the library.
Manage Authors: Add, view, update, and delete authors.
Manage Borrowers: Add, view, update, and delete borrowers.
Manage Borrowed Books: Borrow and return books, view borrowed books.
Prerequisites
Before using the system, ensure that the following software is installed:

Python 3.x
Install Python 3.x if it’s not already installed on your system. You can download Python from the official website here.

MySQL
MySQL (version 5.7 or higher recommended) is required. To install MySQL, follow the steps below:

## On Ubuntu/Debian-based systems:
Copy code
sudo apt update
sudo apt install mysql-server
## Once installed, start MySQL:
Copy code
sudo systemctl start mysql
## Secure the MySQL installation:
Copy code
sudo mysql_secure_installation
Set a password for the MySQL root user when prompted.

## MySQL Connector for Python
You need the mysql-connector-python package to interact with MySQL in Python. To install it, run:
Copy code
pip install mysql-connector-python
Installation Steps
1. Install MySQL Server
Follow the installation steps mentioned above under the "MySQL" section to install MySQL on your system.

2. Install Python and Dependencies
Ensure Python 3.x is installed on your system. If not, install it as follows:
Copy code
sudo apt install python3 python3-pip
## Next, create a virtual environment and install the required dependencies:
Copy code
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install MySQL connector for Python
pip install mysql-connector-python
3. Create the Database and Tables
## Log into MySQL to create the database and the required tables:
Copy code
sudo mysql -u root -p
## Once logged in, execute the following SQL commands:
sql
Copy code
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
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL
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
4. Configure MySQL Connection
Ensure that the MySQL connection details are correctly set in the code (in db.py or a similar file):

python
Copy code
import mysql.connector

def get_connection():
    """Establish and return a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host='localhost',
        database='LibraryManagementSystem',  # Database name
        user='root',  # MySQL user
        password='1234'  # MySQL password
    )
    return connection
5. Run the Application
Once your database is set up, and the dependencies are installed, run the main.py file to launch the interactive CLI:
Copy code
python3 main.py
Usage
1. Menu Options
Once the program starts, you’ll see a menu with the following options:

text
Copy code
1. Manage Books
2. Manage Authors
3. Manage Borrowers
4. Manage Borrowed Books
5. Exit

2. Manage Books
## Add a Book:
Choose "Manage Books", then select "Add Book". Provide the book title and the author ID.

## View Books:
Choose "Manage Books", then select "View Books" to view all books in the library.

## Update a Book:
Choose "Manage Books", then select "Update Book". Provide the book ID and new title.

## Delete a Book:
Choose "Manage Books", then select "Delete Book". Provide the book ID to delete the book from the system.

3. Manage Authors
## Add Author:
Choose "Manage Authors", then select "Add Author". Provide the author's name.

## View Authors:
Choose "Manage Authors", then select "View Authors" to view a list of all authors.

## Update Author:
Choose "Manage Authors", then select "Update Author". Provide the author ID and new name.

## Delete Author:
Choose "Manage Authors", then select "Delete Author". Provide the author ID to delete the author.

4. Manage Borrowers
## Add Borrower:
Choose "Manage Borrowers", then select "Add Borrower". Provide the borrower’s name, email, and phone number.

## View Borrowers:
Choose "Manage Borrowers", then select "View Borrowers" to see all borrowers.

## Update Borrower:
Choose "Manage Borrowers", then select "Update Borrower". Provide the borrower ID and new details.

## Delete Borrower:
Choose "Manage Borrowers", then select "Delete Borrower". Provide the borrower ID to delete the borrower.

5. Manage Borrowed Books
## Borrow Book:
Choose "Manage Borrowed Books", then select "Borrow Book". Enter the book ID, borrower ID, and the borrow date.

## Return Book:
Choose "Manage Borrowed Books", then select "Return Book". Provide the borrowed book ID and return date.

## View Borrowed Books:
Choose "Manage Borrowed Books", then select "View Borrowed Books" to see all borrowed books with their borrow and return dates.

6. Exit
To exit the application, simply select "Exit" from the main menu.

Example Usage
Adding a New Book:
Choose "Manage Books".
Choose "Add Book".
Enter the book title (e.g., "The Great Gatsby").
Enter the author ID (e.g., "1").
Viewing Books:
Choose "Manage Books".
Choose "View Books" to see all books in the library.
Borrowing a Book:
Choose "Manage Borrowed Books".
Choose "Borrow Book".
Enter the book ID and borrower ID.
Enter the borrow date.
Error Handling
## If the application cannot connect to the MySQL database, check the following:
Ensure MySQL is running.
Verify the database and tables exist.
Check if the MySQL user and password are correctly set in the db.py file.
## To start MySQL, run:
Copy code
sudo systemctl start mysql
## If MySQL doesn’t start, check its status:
Copy code
sudo systemctl status mysql
## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit pull requests. To contribute:
Fork the repository.
Create a new bra
Copy code
git checkout -b feature-branch
Commit your changes:
Copy code
git commit -am 'Add new feature'
Push to the branch:
Copy code
git push origin feature-branch
Submit a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Access MySQL Command Line
You can access the MySQL command line interface with:
Copy code
mysql -u root -p
## links
## github link ->https://github.com/jameskimani001/Library-Management-System

## Slides link -> https://docs.google.com/presentation/d/1ctgVVEEGxy13lYeBmBEneOOGD-PFYJepjYsR5xGr7_g/edit#slide=id.g2d7210c904c_0_654

## video link ->https://app.screencastify.com/v2/manage/videos/fkgMn9Rkdn9I8OPcVwG7
## Coded with passion and love by Techie Kim. 😊