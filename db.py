import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='LibraryManagementSystem',  # Specify your database here
            user='root',  # MySQL root user
            password='1234'  # New password
        )
        
        # Check if the connection is successful
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
        else:
            print("Failed to connect to the database.")
            return None

    except Error as e:
        print(f"Error: {e}")
        return None
