from random import shuffle


class Game:
    def __init__(self, tiles, players):
        self.players = players
        shuffle(self.players)
        self.tiles = tiles
        self.shuffle_tiles()
        self.played_tiles = []
        self.played_tiles.append(self.tiles.pop())
        self.distribute_tiles()
        print(f'Game starting with the first tile: <{self.played_tiles[0].side1}:{self.played_tiles[0].side2}>')

    def shuffle_tiles(self):
        shuffle(self.tiles)

    def distribute_tiles(self):
        for player in self.players:
            player.tiles.extend([self.tiles.pop(0) for tile in range(6)])

    def players_have_tiles(self):
        return len(list(filter(lambda player: len(player.tiles) > 0, self.players))) == len(self.players)

    def start(self):
        self.players[0].can_play = True
        while True:
            for player in self.players:
                player.play(self.played_tiles, self.tiles)
                if len(player.tiles) == 0:
                    print(f'Player {player.name} has won!')
                    return
