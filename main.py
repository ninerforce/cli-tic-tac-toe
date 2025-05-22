import board
import ai  

def main():
    print("Welcome to Tic Tac Toe, please pick a side (crosses play first)")
    side = input("> ").strip().lower()

    if side not in ["crosses", "naughts"]:
        print("Please pick a valid side (naughts or crosses)")
        return

    player_side = side
    ai_side = "naughts" if player_side == "crosses" else "crosses"
    player_symbol = "X" if player_side == "crosses" else "O"
    ai_symbol = "X" if ai_side == "crosses" else "O"

    game_board = board.Board()
    ai_opponent = ai.opponent(ai_side)
    current_turn = "crosses"

    while True:
        game_board.print_board()
        winner = game_board.detect_win()
        if winner:
            print(f"{'Crosses' if winner == 'X' else 'Naughts'} win!")
            break

        # Check for draw
        if all(cell != "." for row in game_board.board for cell in row):
            print("It's a draw!")
            break

        if current_turn == player_side:
            print("Your move (e.g. a1, b2):")
            move = input("> ").strip().lower()
            try:
                game_board.place_piece(player_side, move)
                current_turn = ai_side
            except ValueError:
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            move = ai_opponent.get_ai_move(game_board) 
            print(f"AI plays: {move}")
            game_board.place_piece(ai_side, move)
            current_turn = player_side

if __name__ == "__main__":
    main()

    