# Tic-Tac-Toe
<img src="images\tic-tac-toe-image.png" alt="Tic-tac-toe logo" width="300" height="200">


In this project your job is to implement Tic-Tac-Toe for two players. You also can try writing some AI to play the game. If you find it easy, try to make it unbeatable.


## Initialize the board
Implement get_empty_board() to return an empty 3-by-3 board, a list of lists filled with dots. The inner lists are rows.

1. A list of lists is returned that represents a list of rows.

2. Every cell of the returned value is .

3. The rows of the returned value are independent, changing one row does not affect the others.

4. Printing the result of the get_empty_board() function shows the following in the terminal.

```bash
[ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
```

## Get players' move
Implement get_human_coordinates that asks for user input and returns the coordinates of a valid move on board.

1. The accepts coordinates as a letter and a number: A2 is first row and second column, C1 is third row and first column, and so on.

2. The function returns a tuple of two integers (row, col).

3. The returned coordinates start from 0.

4. The integers indicate a valid (empty) position on the board.

5. The program keeps asking for coordinates if the coordinates provided are outside of board.

6. The program keeps asking for coordinates if the coordinates provided are taken.

7. The program keeps asking for coordinates if the coordinates provided do not match the format.


## Implement making a move

When the user has chosen a coordinate, that place is marked on the board.

1. If the cell at row and col is empty (contains a dot .), it is marked with player.

2. Out-of-bounds coordinates are not interpreted as moves.

3. Coordinates of already occupied cells are not interpreted as moves.



## Check for winners

Implement get_winning_player() that returns X or O based on the winning player has three of their marks in a horizontal, vertical, or diagonal row on board.

1. The get_winning_player() function returns X if X has a three-in-a-row on board.

2. The get_winning_player() function returns None if there is no three-in-a-row on the board


## Check for a full board
Implement is_board_full that returns True if the board is full.

1. The is_board_full function returns True if there are no empty cells on the board.

2. The is_board_full() returns False if there are empty cells on the board.

## Print board
Implement display_board() that prints the board to the screen.

1. Players are indicated with X and 0. Empty fields are indicated with dots (.).

2. Coordinates are displayed around the board.

3. The board is displayed in the following format:

```bash
   1   2   3
A  . | . | .
  ---+---+---
B  . | . | .
  ---+---+---
C  . | . | .
```


## Print result
The game shows if X or O or no one has won the game

1. If player X wins, "X has won!" is displayed.

2. If player 0 wins, "0 has won!" is displayed.

3. If nobody wins, "It's a tie!" is displayed


## Game logic
Implement all the functions so that the game will run successfully

1. Player X starts the game.

2. Players alternate their moves (X, 0, X, 0...).

3. The board is displayed before each move, and at the end of game.

4. The game ends when someone wins or the board is full.

5. The game handles bad input (wrong coordinates) without crashing.



## Hints
- You don't have to come up with an AI strategy. You can search the internet for strategy descriptions. Do not use external code; implement written instructions instead.

- You don't have to implement a general playing strategy. Tic-Tac-Toe has a rather easy unbeatable strategy that can be expressed as a sequence of conditionals.