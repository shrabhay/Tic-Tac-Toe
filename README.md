# Tic Tac Toe
## Overview
This project is a simple command-line-based implementation of the classic Tic Tac Toe game written in Python. It allows two players to play alternately, keeping track of their scores across multiple rounds.

---

## Features
* **Interactive Gameplay**: Players take turns to place their markers ('X' or 'O') on a 3x3 board.
* **Winner Detection**: The script checks for winning conditions (rows, columns, or diagonals) after every move.
* **Score Tracking**: The game keeps track of the total wins for both players.
* **Dynamic Turns**: Alternates between players for each round.
* **Replayability**: Players can choose to replay after each game ends.
* **Tie Handling**: Properly detects and announces ties when the board is full.

---

## How to Use
1. Clone the repository or download the `tic_tac_toe.py` file.
2. Open a terminal and navigate to the directory containing the file.
3. Run the script with the command:
    ```commandline
    python tic_tac_toe.py
    ```

4. Follow the on-screen prompts to play the game.

---

## Rules
1. The game is played on a 3x3 grid.
2. Players take turns to place their marker (X or O) by selecting a number between 1 and 9, corresponding to the grid's positions:
    ```markdown
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    ```
 
3. A player wins by aligning three of their markers in a row, column, or diagonal.
4. If the board is filled without a winner, the game ends in a tie.

---

## Requirements
* Python 3.x
* No external libraries are required.

---

## Example Gameplay
```commandline
Would you like to play a game of TIC TAC TOE? Enter 'Y' or 'N': y
 |   |  
_________
 |   |  
_________
 |   |  
Player X, enter your move (1 - 9): 5
 |   |  
_________
 | X |  
_________
 |   |  
Player O, enter your move (1 - 9): 1
O |   |  
_________
 | X |  
_________
 |   |  
...
```

---

## Customization
Feel free to modify the code to:

* Add an AI player.
* Enhance the UI (e.g., graphical representation using a library like Tkinter or Pygame).
* Save game progress.

---

## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

---

## License
This project is licensed under the MIT License.