def algebraic_to_coords(algebraic: str):
    if len(algebraic) !=2:
        return ValueError("Incorrect move format")

    file = algebraic[0]
    rank = algebraic[1]

    if file not in 'abc' or rank not in '123':
            raise ValueError(f"Invalid square: {square}")

    col = ord(file) - ord('a')
    row = 3 - int(rank)

    return [row, col]

def coords_to_algebraic(coords: list):
    row, col = coords

    if not (0 <= row < 3 and 0 <= col < 3):
        raise ValueError(f"Invalid board coordinates: {coords}")

    file = chr(ord('a') + col)       # Converts 0 → 'a', 1 → 'b', 2 → 'c'
    rank = str(3 - row)              # Converts 0 → '3', 1 → '2', 2 → '1'

    return file + rank