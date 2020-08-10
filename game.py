import itertools
import copy

US = 1
THEM = -1

directions = list(itertools.product(range(-1, 2), range(-1, 2)))
directions.remove((0, 0))

def add_direction(src, direction):
    return (src[0] + direction[0], src[1] + direction[1])

class Board:
    def __init__(self, source):
        self.contents = copy.deepcopy(source)
        self.all_tiles = list(itertools.product(range(8), range(8)))
    
    def get_tile_at(self, pos):
        x, y = pos
        return self.contents[x][y]

    def set_tile_at(self, pos, value):
        x, y = pos
        self.contents[x][y] = value

    def in_bounds(self, v):
        return v in range(0, 8)
    
    def get_flipped_tiles(self, player, x, y):
        opponent = -player

        flipped_tiles = []

        for d in directions:
            first = True
            focus = (x, y)
            found_end = False
            path = []

            while (self.get_tile_at(focus) == opponent) or first:
                first = False

                focus = add_direction(focus, d)

                if (not self.in_bounds(focus[0])) or (not self.in_bounds(focus[1])):
                    break

                if self.get_tile_at(focus) == player:
                    found_end = True
                    break
                elif self.get_tile_at(focus) == opponent:
                    path.append(focus)

            if found_end:
                flipped_tiles += path
        
        return flipped_tiles

    def check_legal(self, player, move):
        if self.get_tile_at(move) == 0:
            flipped_tiles = self.get_flipped_tiles(player, *move)
            return len(flipped_tiles) > 0
        else:
            return False

    def get_legal_moves(self, player):
        moves = []
        for tile in self.all_tiles:
            if self.check_legal(player, tile):
                moves.append(tile)
        return moves

    def flip_tiles(self, tiles):
        for t in tiles:
            self.set_tile_at(t, -self.get_tile_at(t))

    def put_move(self, player, move):
        if self.check_legal(player, move):
            self.flip_tiles(self.get_flipped_tiles(player, *move))

    def with_move(self, player, move):
        if self.check_legal(player, move):
            new_board = Board(self.contents)
            new_board.put_move(player, move)
            return new_board
        else:
            return None
