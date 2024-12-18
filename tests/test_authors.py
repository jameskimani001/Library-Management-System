# tests/test_authors.py
import unittest
from authors import add_author, view_authors, update_author, delete_author
from create_tables import get_connection
import mysql.connector

class TestAuthors(unittest.TestCase):

    def setUp(self):
        """Setup for tests - create a test author."""
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO authors (name, birth_date) VALUES ('Test Author', '1980-01-01')")
        self.connection.commit()

    def tearDown(self):
        """Tear down after tests - delete test author."""
        self.cursor.execute("DELETE FROM authors WHERE name = 'Test Author'")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def test_add_author(self):
        """Test adding an author."""
        add_author("New Author", "1990-05-05")
        self.cursor.execute("SELECT * FROM authors WHERE name = 'New Author'")
        author = self.cursor.fetchone()
        self.assertIsNotNone(author)

    def test_view_authors(self):
        """Test viewing all authors."""
        authors = view_authors()
        self.assertGreater(len(authors), 0)

    def test_update_author(self):
        """Test updating an author's details."""
        self.cursor.execute("SELECT * FROM authors WHERE name = 'Test Author'")
        author = self.cursor.fetchone()
        update_author(author[0], "Updated Author", "1985-06-15")
        self.cursor.execute("SELECT * FROM authors WHERE id = %s", (author[0],))
        updated_author = self.cursor.fetchone()
        self.assertEqual(updated_author[1], "Updated Author")

    def test_delete_author(self):
        """Test deleting an author."""
        self.cursor.execute("SELECT * FROM authors WHERE name = 'Test Author'")
        author = self.cursor.fetchone()
        delete_author(author[0])
        self.cursor.execute("SELECT * FROM authors WHERE id = %s", (author[0],))
        deleted_author = self.cursor.fetchone()
        self.assertIsNone(deleted_author)

if __name__ == "__main__":
    unittest.main()
