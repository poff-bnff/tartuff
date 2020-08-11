# test_fetch_data.py
import fetch_data
import unittest
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_credsFunction(self):
        """
        Test that creds exists
        """
        result = fetch_data.credsFunction()
        self.assertNotEqual(result, None)

if __name__ == '__main__':
    unittest.main()
