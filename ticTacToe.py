#!/usr/bin/env python3

class ticTacToe:
    def __init__(self) -> None:

        # this is the gameboard
        self.board = [
            " "," "," ",
            " "," "," ",
            " "," "," "
        ]
    
    def move(self, x: int, y: int, player: str) -> None:
        ptr = x + (y * 3) # this variable marks what space the x or o will be placed

        self.board[ptr] = player
    
    # checks if a player has won
    # make more readable later
    def checkWin(self, player: str) -> str or bool:
        if self.board[0] and self.board[1] and self.board[2] == "x":
            return "x"
        elif self.board[3] and self.board[4] and self.board[5] == "x":
            return "x"
        elif self.board[6] and self.board[7] and self.board[8] == "x":
            return "x"
        elif self.board[2] and self.board[4] and self.board[6] == "x":
            return "x"
        elif self.board[0] and self.board[4] and self.board[8] == "x":
            return "x"
        elif self.board[0] and self.board[3] and self.board[6] == "x":
            return "x"
        elif self.board[1] and self.board[4] and self.board[7] == "x":
            return "x"
        elif self.board[2] and self.board[5] and self.board[8] == "x":
            return "x"
        elif self.board[0] and self.board[1] and self.board[2] == "o":
            return "o"
        elif self.board[3] and self.board[4] and self.board[5] == "x":
            return "o"
        elif self.board[6] and self.board[7] and self.board[8] == "o":
            return "o"
        elif self.board[2] and self.board[4] and self.board[6] == "x":
            return "o"
        elif self.board[0] and self.board[4] and self.board[8] == "o":
            return "o"
        elif self.board[0] and self.board[3] and self.board[6] == "o":
            return "o"
        elif self.board[1] and self.board[4] and self.board[7] == "o":
            return "o"
        elif self.board[2] and self.board[5] and self.board[8] == "o":
            return "o"
        else:
            return False