# tests/test_books.py
import unittest
from books import add_book, view_books, update_book, delete_book
from create_tables import get_connection

class TestBooks(unittest.TestCase):

    def setUp(self):
        """Setup for tests - create a test book."""
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO books (title, author_id, genre, published_year) VALUES ('Test Book', 1, 'Fiction', 2020)")
        self.connection.commit()

    def tearDown(self):
        """Tear down after tests - delete test book."""
        self.cursor.execute("DELETE FROM books WHERE title = 'Test Book'")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def test_add_book(self):
        """Test adding a book."""
        add_book("New Book", 1, "Science", 2022)
        self.cursor.execute("SELECT * FROM books WHERE title = 'New Book'")
        book = self.cursor.fetchone()
        self.assertIsNotNone(book)

    def test_view_books(self):
        """Test viewing all books."""
        books = view_books()
        self.assertGreater(len(books), 0)

    def test_update_book(self):
        """Test updating a book's details."""
        self.cursor.execute("SELECT * FROM books WHERE title = 'Test Book'")
        book = self.cursor.fetchone()
        update_book(book[0], "Updated Book", book[2], book[3], 2021)
        self.cursor.execute("SELECT * FROM books WHERE id = %s", (book[0],))
        updated_book = self.cursor.fetchone()
        self.assertEqual(updated_book[1], "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        self.cursor.execute("SELECT * FROM books WHERE title = 'Test Book'")
        book = self.cursor.fetchone()
        delete_book(book[0])
        self.cursor.execute("SELECT * FROM books WHERE id = %s", (book[0],))
        deleted_book = self.cursor.fetchone()
        self.assertIsNone(deleted_book)

if __name__ == "__main__":
    unittest.main()
