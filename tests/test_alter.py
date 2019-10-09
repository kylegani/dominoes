import unittest

from utilities.alter import flipped
from classes.tile import Tile


class TestFlipped(unittest.TestCase):
    data = Tile(5, 4)

    def test_flipped(self):
        """
        Test that the values of the returned tile are flipped
        """
        result = flipped(self.data)
        self.assertEqual(result.side1, self.data.side2)
        self.assertEqual(result.side2, self.data.side1)

    def test_flipped_type(self):
        """
        Test that it returns a tile
        """
        result = flipped(self.data)
        self.assertIsInstance(result, Tile)

if __name__ == '__main__':
    unittest.main()
