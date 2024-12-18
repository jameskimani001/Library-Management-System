# tests/test_utils.py
import unittest
import utilis

class TestUtils(unittest.TestCase):

    def test_log_info(self):
        """Test info logging."""
        utilis.log_info("This is an info log.")
        # Since the log is printed to console, we may not assert anything here.
        # It can be captured or tested with a more advanced logger test.

    def test_log_error(self):
        """Test error logging."""
        utilis.log_error("This is an error log.")
        # Similarly, we could capture the log for further testing.
        
if __name__ == "__main__":
    unittest.main()
