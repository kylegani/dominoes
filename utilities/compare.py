from utilities import find
from utilities.alter import flipped


def matches_left(tile1, tile2):
    return tile1.side2 == tile2.side1


def matches_right(tile1, tile2):
    return tile1.side1 == tile2.side2


def is_double(tile):
    return tile.side1 == tile.side2


def is_blocker(tile, played_tiles_ref):
    return (tile.side2 == find.first(played_tiles_ref).side1 and tile.side1 == find.last(played_tiles_ref).side2)\
           or (tile.side1 == find.last(played_tiles_ref).side2 and tile.side2 == find.first(played_tiles_ref).side1) or\
           (flipped(tile).side2 == find.first(played_tiles_ref).side1 and
            flipped(tile).side1 == find.last(played_tiles_ref).side2) or \
           (flipped(tile).side1 == find.last(played_tiles_ref).side2 and
            flipped(tile).side2 == find.first(played_tiles_ref).side1)
