import unittest

from utilities import compare
from classes.tile import Tile


class TestMatchesLeft(unittest.TestCase):
    tile1 = Tile(4, 5)
    tile2 = Tile(2, 2)
    tile3 = Tile(5, 5)

    def test_matches_left_success(self):
        """
        returns a positive match
        """
        result = compare.matches_left(self.tile1, self.tile3)
        self.assertEqual(result, True)

    def test_matches_left_failure(self):
        """
        returns a negative match
        """
        result = compare.matches_left(self.tile1, self.tile2)
        self.assertEqual(result, False)


class TestMatchesRight(unittest.TestCase):
    tile1 = Tile(5, 4)
    tile2 = Tile(2, 2)
    tile3 = Tile(5, 5)

    def test_matches_right_success(self):
        """
        returns a positive match
        """
        result = compare.matches_right(self.tile1, self.tile3)
        self.assertEqual(result, True)

    def test_matches_right_failure(self):
        """
        returns a negative match
        """
        result = compare.matches_right(self.tile1, self.tile2)
        self.assertEqual(result, False)


class TestIsDouble(unittest.TestCase):
    tile1 = Tile(5, 4)
    tile2 = Tile(2, 2)

    def test_is_double_success(self):
        """
        returns a positive match
        """
        result = compare.is_double(self.tile2)
        self.assertEqual(result, True)

    def test_is_double_failure(self):
        """
        returns a negative match
        """
        result = compare.is_double(self.tile1)
        self.assertEqual(result, False)


class TestIsBlocker(unittest.TestCase):
    tile = Tile(5, 4)
    played_tiles_mismatch = [Tile(2, 2), Tile(4, 4)]
    played_tiles_match = [Tile(4, 2), Tile(2, 5)]

    def test_is_blocker_success(self):
        """
        returns a positive match
        """
        result = compare.is_blocker(self.tile, self.played_tiles_match)
        self.assertEqual(result, True)

    def test_is_blocker_failure(self):
        """
        returns a negative match
        """
        result = compare.is_blocker(self.tile, self.played_tiles_mismatch)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
