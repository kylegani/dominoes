import unittest

from utilities import generate
from classes.tile import Tile


class TestTiles(unittest.TestCase):
    data = [Tile(0, 0), Tile(0, 1), Tile(0, 2), Tile(0, 3), Tile(0, 4), Tile(0, 5), Tile(0, 6), Tile(1, 1), Tile(1, 2),
            Tile(1, 3), Tile(1, 4), Tile(1, 5), Tile(1, 6), Tile(2, 2), Tile(2, 3), Tile(2, 4), Tile(2, 5), Tile(2, 6),
            Tile(3, 3), Tile(3, 4), Tile(3, 5), Tile(3, 6), Tile(4, 4), Tile(4, 5), Tile(4, 6), Tile(5, 5), Tile(5, 6),
            Tile(6, 6)]

    def test_tile_count(self):
        """
        Returns a list of 28 tiles
        """
        result = generate.tiles()
        self.assertEqual(len(result), 28)

    def test_tile_combinations(self):
        """
        Returns the correct combinations of tiles
        """
        result = generate.tiles()
        for i in range(28):
            self.assertTrue(result[i].eq(self.data[i]))

