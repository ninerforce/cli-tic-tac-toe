# CLI Tic Tac Toe
This portfolio project implements a fully playable command-line Tic Tac Toe game featuring:

1. A player vs AI system

2. Optimal AI strategy based on Newell and Simon's decision hierarchy

3. Custom board and move management system

4. Algebraic coordinate interface (e.g., a1, b2)

5. Modular codebase structured for readability and extensibility

## How to Run

Clone or download this repository:

`git clone https://github.com/ninerforce/cli-tic-tac-toe.git`

`cd cli-tic-tac-toe`

Run the game:

`python main.py`

Choose your side: "crosses" or "naughts"

### Sample Gameplay

    Welcome to Tic Tac Toe, please pick a side (crosses play first)
    > crosses

      +-------+
    3 | . . . |
    2 | . . . |
    1 | . . . |
      +-------+
        a b c

    Your move (e.g. a1, b2):
    > b2

      +-------+
    3 | . . . |
    2 | . X . |
    1 | . . . |
      +-------+
        a b c

    AI is thinking...
    ...



### Why This is a Valuable Portfolio Project

#### Showcases Core CS Skills

1. **Object Oriented Programming Best Practices**
2. **Algorithmic Thinking**
3. **Validation & Input Handling:**

#### Implementation of Simple AI

1. AI always plays **perfectly**.
2. Implements an ordered rule-based system (based on Newell and Simon) aligned with how humans approach structured problems.

### Acknowledgements

AI Algorithm based on the work of Newell and Simon, which was further described by Crowley and Siegler at https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1704_3