from utilities import compare
from utilities.alter import flipped


def matching_tile(tile, played_tiles):
    return compare.matches_left(tile, first(played_tiles)) or \
           compare.matches_left(flipped(tile), first(played_tiles)) or \
           compare.matches_right(tile, last(played_tiles)) or \
           compare.matches_right(flipped(tile), last(played_tiles))


def exists(tile, tiles):
    return len(list(filter(lambda iterator: (iterator.side1 == tile.side1 and iterator.side2 == tile.side2) or
                                            (flipped(iterator).side1 == tile.side2 and
                                             flipped(iterator).side2 == tile.side2), tiles))) > 0


def first(played_tiles):
    return played_tiles[0]


def last(played_tiles):
    return played_tiles[len(played_tiles) - 1]
