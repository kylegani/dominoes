from classes.tile import Tile


def tiles():
    dominoes = []
    for side1 in range(7):
        for side2 in range(7):
            dominoes.append(Tile(side1, side2))
    return dominoes
