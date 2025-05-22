import utils

initial_board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

class Board:

    def __init__(self):
        self.board = initial_board

    def print_board(self):
        print("  +-------+")
        for row in range(3):
            print(f"{3 - row} |", end=" ")
            for col in range(3):
                piece = self.board[row][col]
                print(piece, end=" ")
            print("|")
        print("  +-------+")
        print("    a b c")

    def get_piece(self, coord: list):
        return self.board[coord[0]][coord[1]]

    def place_piece(self, side: str, algebraic_coords: str):
        piece = "X" if (side=="crosses") else "O"
        
        coords = utils.algebraic_to_coords(algebraic_coords)

        if self.get_piece(coords) == ".":
            self.board[coords[0]][coords[1]] = piece
        else:
            return ValueError("Invalid Move")

    def detect_win(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] != "." and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]  # Row win
            if self.board[0][i] != "." and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]  # Column win

        # Check diagonals
        if self.board[0][0] != "." and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]  # Main diagonal
        if self.board[0][2] != "." and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]  # Anti-diagonal

        return None  # No winner yet
