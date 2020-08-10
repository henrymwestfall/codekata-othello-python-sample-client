import random

from game import US, THEM

class AI:
    def __init__(self):
        self.name = "Fake Edward"

    def do_move(self, board):
        legal_moves = board.get_legal_moves(US)
        best_move = legal_moves[0]
        flipped_tiles = 0
        for tile in legal_moves:
            tiles = len(board.get_flipped_tiles(US, *tile))
            if tiles > flipped_tiles:
                flipped_tiles = tiles
                best_move = tile
        return best_move