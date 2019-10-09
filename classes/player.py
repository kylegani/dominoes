from utilities import compare, find
from decorators.game_play import can_play
from decorators.output import print_play, print_board

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.can_play = False
        self.available_plays = []

    @can_play
    @print_play
    def draw_tile(self, pile_ref):
        tile = pile_ref[0]
        self.tiles.append(tile)
        self.can_play = False
        pile_ref.remove(tile)
        return f'{self.name} can\'t play. Drawing tile <{tile.side1}:{tile.side2}>'

    @can_play
    @print_play
    @print_board
    def place_tile(self, tile, played_tiles_ref):
        matched_tile = find.first(played_tiles_ref)
        if tile.side1 == matched_tile.side1:
            played_tiles_ref.insert(0, tile.flip())
        elif tile.side2 == matched_tile.side1:
            played_tiles_ref.insert(0, tile)
        elif tile.side1 == find.last(played_tiles_ref).side2:
            matched_tile = find.last(played_tiles_ref)
            played_tiles_ref.append(tile)
        else:
            matched_tile = find.last(played_tiles_ref)
            played_tiles_ref.append(tile.flip())
        return f'{self.name} plays <{tile.side1}:{tile.side2}> to connect to tile ' \
               f'<{matched_tile.side1}:{matched_tile.side2}> on the board.'

    @can_play
    def play_highest_double(self, played_tiles_ref):
        doubles = [tile for tile in self.tiles if compare.is_double(tile) and find.matching_tile(tile, played_tiles_ref)]
        doubles.sort(key=lambda tile: tile.side1)
        if not len(doubles):
            return False
        self.place_tile(doubles[0], played_tiles_ref)
        self.tiles.remove(doubles[0])
        self.can_play = False
        return True

    @can_play
    def play_blocker(self, played_tiles_ref):
        blockers = [tile for tile in self.tiles if compare.is_blocker(tile, played_tiles_ref)]
        if not len(blockers):
            return False
        self.place_tile(blockers[0], played_tiles_ref)
        self.tiles.remove(blockers[0])
        self.can_play = False
        return True

    @can_play
    def play_highest_tile(self, played_tiles_ref):
        tiles = [tile for tile in self.tiles if find.matching_tile(tile, played_tiles_ref)]
        tiles.sort(key=lambda tile: tile.tally())
        if len(tiles) < 1:
            return False
        self.place_tile(tiles[0], played_tiles_ref)
        self.tiles.remove(tiles[0])
        self.can_play = False
        return True

    def play(self, played_cards_ref, pile_ref):
        self.can_play = True
        self.play_highest_double(played_cards_ref)
        self.play_blocker(played_cards_ref)
        self.play_highest_tile(played_cards_ref)
        self.draw_tile(pile_ref)
