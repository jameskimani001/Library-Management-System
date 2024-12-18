# tests/test_borrowers.py
import unittest
from borrowers import add_borrower, view_borrowers, update_borrower, delete_borrower
from create_tables import get_connection

class TestBorrowers(unittest.TestCase):

    def setUp(self):
        """Setup for tests - create a test borrower."""
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO users (name, email, phone) VALUES ('Test Borrower', 'test@example.com', '123456789')")
        self.connection.commit()

    def tearDown(self):
        """Tear down after tests - delete test borrower."""
        self.cursor.execute("DELETE FROM users WHERE name = 'Test Borrower'")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def test_add_borrower(self):
        """Test adding a borrower."""
        add_borrower("New Borrower", "new@example.com", "987654321")
        self.cursor.execute("SELECT * FROM users WHERE name = 'New Borrower'")
        borrower = self.cursor.fetchone()
        self.assertIsNotNone(borrower)

    def test_view_borrowers(self):
        """Test viewing all borrowers."""
        borrowers = view_borrowers()
        self.assertGreater(len(borrowers), 0)

    def test_update_borrower(self):
        """Test updating a borrower's details."""
        self.cursor.execute("SELECT * FROM users WHERE name = 'Test Borrower'")
        borrower = self.cursor.fetchone()
        update_borrower(borrower[0], "Updated Borrower", "updated@example.com", "1122334455")
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (borrower[0],))
        updated_borrower = self.cursor.fetchone()
        self.assertEqual(updated_borrower[1], "Updated Borrower")

    def test_delete_borrower(self):
        """Test deleting a borrower."""
        self.cursor.execute("SELECT * FROM users WHERE name = 'Test Borrower'")
        borrower = self.cursor.fetchone()
        delete_borrower(borrower[0])
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (borrower[0],))
        deleted_borrower = self.cursor.fetchone()
        self.assertIsNone(deleted_borrower)

if __name__ == "__main__":
    unittest.main()
