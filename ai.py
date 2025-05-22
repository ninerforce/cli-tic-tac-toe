import utils
import copy

class opponent:
    def __init__(self, side):
        self.side = side
        self.ai_piece = "X" if side == "crosses" else "O"
        self.opponent_piece = "O" if self.ai_piece == "X" else "X"

    def get_ai_move(self, board_obj):
        for strategy in [
            self.look_for_win,
            self.look_for_block,
            self.look_for_fork,
            self.block_fork,
            self.play_centre,
            self.play_opposite_corner,
            self.play_empty_corner,
            self.play_empty_side
        ]:
            move = strategy(board_obj)
            if move:
                return move
        return None

    def look_for_win(self, board_obj):
        return self.find_winning_move(board_obj, self.ai_piece)

    def look_for_block(self, board_obj):
        return self.find_winning_move(board_obj, self.opponent_piece)

    def find_winning_move(self, board_obj, piece):
        for row in range(3):
            for col in range(3):
                if board_obj.board[row][col] == ".":
                    board_obj.board[row][col] = piece
                    if board_obj.detect_win() == piece:
                        board_obj.board[row][col] = "."
                        return utils.coords_to_algebraic([row, col])
                    board_obj.board[row][col] = "."
        return None

    def look_for_fork(self, board_obj):
        return self.find_fork(board_obj, self.ai_piece)

    def block_fork(self, board_obj):
        return self.find_fork(board_obj, self.opponent_piece)

    def find_fork(self, board_obj, piece):
        for row in range(3):
            for col in range(3):
                if board_obj.board[row][col] == ".":
                    board_obj.board[row][col] = piece
                    win_count = 0
                    for r in range(3):
                        for c in range(3):
                            if board_obj.board[r][c] == ".":
                                board_obj.board[r][c] = piece
                                if board_obj.detect_win() == piece:
                                    win_count += 1
                                board_obj.board[r][c] = "."
                    board_obj.board[row][col] = "."
                    if win_count >= 2:
                        return utils.coords_to_algebraic([row, col])
        return None

    def play_centre(self, board_obj):
        if board_obj.board[1][1] == ".":
            return utils.coords_to_algebraic([1,1])
        return None

    def play_opposite_corner(self, board_obj):
        corners = [([0,0],[2,2]), ([0,2],[2,0]), ([2,0],[0,2]), ([2,2],[0,0])]
        for opp_corner, my_corner in corners:
            if board_obj.board[opp_corner[0]][opp_corner[1]] == self.opponent_piece and board_obj.board[my_corner[0]][my_corner[1]] == ".":
                return utils.coords_to_algebraic(my_corner)
        return None

    def play_empty_corner(self, board_obj):
        for coord in [[0,0], [0,2], [2,0], [2,2]]:
            if board_obj.board[coord[0]][coord[1]] == ".":
                return utils.coords_to_algebraic(coord)
        return None

    def play_empty_side(self, board_obj):
        for coord in [[0,1], [1,0], [1,2], [2,1]]:
            if board_obj.board[coord[0]][coord[1]] == ".":
                return utils.coords_to_algebraic(coord)
        return None
