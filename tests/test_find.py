import unittest

from utilities import find
from classes.tile import Tile


class TestFlipped(unittest.TestCase):
    data = [Tile(5, 4), Tile(4, 5)]

    def test_matching_tile(self):
        """
        Returns a successful match
        """
        result = find.matching_tile(self.data[0], self.data)
        self.assertEqual(result, True)

    def test_flipped_type(self):
        """
        Returns an unsuccessful match
        """
        result = find.matching_tile(Tile(1, 1), self.data)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
