from utilities import compare
from utilities.alter import flipped


def matching_tile(tile, played_tiles):
    return compare.matches_left(tile, first(played_tiles)) or \
           compare.matches_left(flipped(tile), first(played_tiles)) or \
           compare.matches_right(tile, last(played_tiles)) or \
           compare.matches_right(flipped(tile), last(played_tiles))


def first(played_tiles):
    return played_tiles[0]


def last(played_tiles):
    return played_tiles[len(played_tiles) - 1]
