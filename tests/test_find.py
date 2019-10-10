import unittest

from utilities import find
from classes.tile import Tile


class TestMatchingTile(unittest.TestCase):
    data = [Tile(5, 4), Tile(4, 5)]

    def test_matching_tile(self):
        """
        Returns a successful match
        """
        result = find.matching_tile(self.data[0], self.data)
        self.assertEqual(result, True)

    def test_non_matching_tile(self):
        """
        Returns an unsuccessful match
        """
        result = find.matching_tile(Tile(1, 1), self.data)
        self.assertEqual(result, False)


class TestExists(unittest.TestCase):
    tiles = [Tile(5, 4), Tile(4, 5)]

    def test_tile_exists(self):
        """
        Returns a successful match
        """
        result = find.exists(self.tiles[0], self.tiles)
        self.assertEqual(result, True)

    def test_does_not_exist(self):
        """
        Returns an unsuccessful match
        """
        result = find.exists(Tile(1, 1), self.tiles)
        self.assertEqual(result, False)


class TestFirst(unittest.TestCase):
    tiles = [Tile(5, 4), Tile(4, 5)]

    def test_first(self):
        """
        Returns the first tile in a list of tiles
        """
        result = find.first(self.tiles)
        self.assertEqual(result, self.tiles[0])


class TestLast(unittest.TestCase):
    tiles = [Tile(5, 4), Tile(4, 5)]

    def test_last(self):
        """
        Returns the last tile in a list of tiles
        """
        result = find.last(self.tiles)
        self.assertEqual(result, self.tiles[-1])

if __name__ == '__main__':
    unittest.main()
