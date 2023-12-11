import unittest
from unittest import result
import random_game_with_sys

class TestMain(unittest.TestCase):

    def test_input(self):
        result = random_game_with_sys.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = random_game_with_sys.run_guess(3, 8)
        self.assertFalse(result)

    def test_input_out_of_bounds(self):
        result = random_game_with_sys.run_guess(12, 8)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()