# tests/test_borrowed_books.py
import unittest
from borrowed_books import borrow_book, return_book, view_borrowed_books
from create_tables import get_connection
from datetime import date

class TestBorrowedBooks(unittest.TestCase):

    def setUp(self):
        """Setup for tests - create a test borrow transaction."""
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO transactions (user_id, book_id, borrow_date) VALUES (1, 1, '2024-12-16')")
        self.connection.commit()

    def tearDown(self):
        """Tear down after tests - delete test borrow transaction."""
        self.cursor.execute("DELETE FROM transactions WHERE user_id = 1 AND book_id = 1")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def test_borrow_book(self):
        """Test borrowing a book."""
        borrow_book(1, 2)  # Borrow book with ID 2
        self.cursor.execute("SELECT * FROM transactions WHERE user_id = 1 AND book_id = 2")
        transaction = self.cursor.fetchone()
        self.assertIsNotNone(transaction)

    def test_return_book(self):
        """Test returning a book."""
        self.cursor.execute("SELECT * FROM transactions WHERE user_id = 1 AND book_id = 1")
        transaction = self.cursor.fetchone()
        return_book(1, 1)
        self.cursor.execute("SELECT * FROM transactions WHERE user_id = 1 AND book_id = 1")
        returned_transaction = self.cursor.fetchone()
        self.assertIsNotNone(returned_transaction)
        self.assertEqual(returned_transaction[4], date.today().strftime('%Y-%m-%d'))

    def test_view_borrowed_books(self):
        """Test viewing borrowed books."""
        transactions = view_borrowed_books()
        self.assertGreater(len(transactions), 0)

if __name__ == "__main__":
    unittest.main()
