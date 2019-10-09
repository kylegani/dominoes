from classes.player import Player
from classes.game import Game
from utilities import generators


def main():
    player1 = Player('Alice')
    player2 = Player('Bob')
    game = Game(generators.tiles(), [player1, player2])
    game.start()


if __name__ == '__main__':
    main()
