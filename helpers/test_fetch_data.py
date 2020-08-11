# test_fetch_data.py
import fetch_data
import unittest
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = fetch_data.credsFunction(3, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
