from classes.player import Player
from classes.game import Game
from utilities import generate


def main():
    player1 = Player('Alice')
    player2 = Player('Bob')
    game = Game(generate.tiles(), [player1, player2])
    game.start()


if __name__ == '__main__':
    main()
