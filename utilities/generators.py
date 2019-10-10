from classes.tile import Tile
from utilities import find


def tiles():
    dominoes = []
    for side1 in range(7):
        for side2 in range(7):
            tile = Tile(side1, side2)
            if not find.exists(tile, dominoes):
                print('adding:', tile.side1, tile.side2)
                dominoes.append(tile)
    print(len(dominoes))
    return dominoes
