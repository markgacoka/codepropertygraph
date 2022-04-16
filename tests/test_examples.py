import os
import unittest
from os.path import exists

BASE_PATH = os.getcwd()

class TestPaths(unittest.TestCase):
    def test_addition_script(self):
        """
        Test if the addition script exists.
        """
        file_exists = exists(BASE_PATH + '\examples\\addition.py')
        self.assertTrue(file_exists)

if __name__ == '__main__':
    unittest.main()