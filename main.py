"""Chess game."""

import time
import math
import random
import json
import operator
import numpy as np

# import pgn


from matrix import coordination, valid_case

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinter import messagebox

SIZE = 64
from tkinter import *

global count
count = 0


class Board:
    """ class for chessboard"""

    def __init__(self, height, width, color="#815426"):
        self.height = height
        self.width = width
        self.color = color
        self.turn = 0
        self.passant = 0
        self.count_step = 0

        self.a = tk.PhotoImage(file="img/a.png")
        self.b = tk.PhotoImage(file="img/b.png")
        self.c = tk.PhotoImage(file="img/c.png")
        self.d = tk.PhotoImage(file="img/d.png")
        self.e = tk.PhotoImage(file="img/e.png")
        self.f = tk.PhotoImage(file="img/f.png")
        self.g = tk.PhotoImage(file="img/g.png")
        self.h = tk.PhotoImage(file="img/h.png")

        self.i1 = tk.PhotoImage(file="img/1.png")
        self.i2 = tk.PhotoImage(file="img/2.png")
        self.i3 = tk.PhotoImage(file="img/3.png")
        self.i4 = tk.PhotoImage(file="img/4.png")
        self.i5 = tk.PhotoImage(file="img/5.png")
        self.i6 = tk.PhotoImage(file="img/6.png")
        self.i7 = tk.PhotoImage(file="img/7.png")
        self.i8 = tk.PhotoImage(file="img/8.png")

        self.w_rook = tk.PhotoImage(file="img/w_rook.png")
        self.b_rook = tk.PhotoImage(file="img/b_rook.png")
        self.w_knight = tk.PhotoImage(file="img/w_knight.png")
        self.b_knight = tk.PhotoImage(file="img/b_knight.png")
        self.w_bishop = tk.PhotoImage(file="img/w_bishop.png")
        self.b_bishop = tk.PhotoImage(file="img/b_bishop.png")
        self.w_king = tk.PhotoImage(file="img/w_king.png")
        self.b_king = tk.PhotoImage(file="img/b_king.png")
        self.w_queen = tk.PhotoImage(file="img/w_queen.png")
        self.b_queen = tk.PhotoImage(file="img/b_queen.png")
        self.w_pawn = tk.PhotoImage(file="img/w_pawn.png")
        self.b_pawn = tk.PhotoImage(file="img/b_pawn.png")
        # list for stockage pieces
        self.pieces_list = [
            [Piece("none", "empty") for col in range(8)] for row in range(8)
        ]
        self.images_list = [["None" for col in range(8)] for row in range(8)]
        self.id = None
        self.coordination = coordination
        self.white_checked = False
        self.black_checked = False
        self.bk_location = (0, 4)
        self.wk_location = (7, 4)
        self.create_list()

    def install_in(self, canvas):
        """Création de chessboard."""
        for row in range(10):
            for col in range(10):
                x0 = col * SIZE
                y0 = row * SIZE
                x1 = x0 + SIZE
                y1 = y0 + SIZE
                # create border
                if row == 0 or row == 9 or col == 0 or col == 9:
                    canvas.create_rectangle((x0, y0, x1, y1), fill="#F8F8FF", width=0)
                    # Alphabet
                    if (row == 0 and col == 1) or (row == 9 and col == 1):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.a)
                    elif (row == 0 and col == 2) or (row == 9 and col == 2):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.b)
                    elif (row == 0 and col == 3) or (row == 9 and col == 3):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.c)
                    elif (row == 0 and col == 4) or (row == 9 and col == 4):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.d)
                    elif (row == 0 and col == 5) or (row == 9 and col == 5):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.e)
                    elif (row == 0 and col == 6) or (row == 9 and col == 6):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.f)
                    elif (row == 0 and col == 7) or (row == 9 and col == 7):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.g)
                    elif (row == 0 and col == 8) or (row == 9 and col == 8):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.h)

                    # Numbers
                    elif (col == 0 and row == 1) or (col == 9 and row == 1):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i8)
                    elif (col == 0 and row == 2) or (col == 9 and row == 2):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i7)
                    elif (col == 0 and row == 3) or (col == 9 and row == 3):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i6)
                    elif (col == 0 and row == 4) or (col == 9 and row == 4):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i5)
                    elif (col == 0 and row == 5) or (col == 9 and row == 5):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i4)
                    elif (col == 0 and row == 6) or (col == 9 and row == 6):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i3)
                    elif (col == 0 and row == 7) or (col == 9 and row == 7):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i2)
                    elif (col == 0 and row == 8) or (col == 9 and row == 8):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i1)

                else:
                    canvas.create_rectangle((x0, y0, x1, y1), fill=self.color)
                    if self.color == "#815426":
                        self.color = "#efe4d6"
                    else:
                        self.color = "#815426"

            if self.color == "#815426":
                self.color = "#efe4d6"
            else:
                self.color = "#815426"

    def create_list(self):
        for row in range(8):
            for col in range(8):

                if row == 1:
                    self.pieces_list[row][col] = Piece("black", "pawn")
                elif row == 6:
                    self.pieces_list[row][col] = Piece("white", "pawn")
                elif (row == 0 and col == 0) or (row == 0 and col == 7):
                    self.pieces_list[row][col] = Piece("black", "rook")
                elif (row == 0 and col == 1) or (row == 0 and col == 6):
                    self.pieces_list[row][col] = Piece("black", "knight")
                elif (row == 0 and col == 2) or (row == 0 and col == 5):
                    self.pieces_list[row][col] = Piece("black", "bishop")
                elif row == 0 and col == 3:
                    self.pieces_list[row][col] = Piece("black", "queen")
                elif row == 0 and col == 4:
                    self.pieces_list[row][col] = Piece("black", "king")
                elif (row == 7 and col == 0) or (row == 7 and col == 7):
                    self.pieces_list[row][col] = Piece("white", "rook")
                elif (row == 7 and col == 1) or (row == 7 and col == 6):
                    self.pieces_list[row][col] = Piece("white", "knight")
                elif (row == 7 and col == 2) or (row == 7 and col == 5):
                    self.pieces_list[row][col] = Piece("white", "bishop")
                elif row == 7 and col == 3:
                    self.pieces_list[row][col] = Piece("white", "queen")
                elif row == 7 and col == 4:
                    self.pieces_list[row][col] = Piece("white", "king")
                else:
                    self.pieces_list[row][col] = Piece("none", "empty")

    def install_pieces(self, canvas):
        """Set up pieces."""
        for row in range(8):
            y = (SIZE * (row + 1)) + 8
            # new = []
            for col in range(8):
                x = (SIZE * (col + 1)) + 8
                if row == 1:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_pawn)
                    self.images_list[row][col] = self.id
                elif row == 6:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_pawn)
                    self.images_list[row][col] = self.id
                elif (row == 0 and col == 0) or (row == 0 and col == 7):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_rook)
                    self.images_list[row][col] = self.id
                elif (row == 0 and col == 1) or (row == 0 and col == 6):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_knight)
                    self.images_list[row][col] = self.id
                elif (row == 0 and col == 2) or (row == 0 and col == 5):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_bishop)
                    self.images_list[row][col] = self.id
                elif row == 0 and col == 3:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_queen)
                    self.images_list[row][col] = self.id
                elif row == 0 and col == 4:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_king)
                    self.images_list[row][col] = self.id
                elif (row == 7 and col == 0) or (row == 7 and col == 7):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_rook)
                    self.images_list[row][col] = self.id
                elif (row == 7 and col == 1) or (row == 7 and col == 6):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_knight)
                    self.images_list[row][col] = self.id
                elif (row == 7 and col == 2) or (row == 7 and col == 5):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_bishop)
                    self.images_list[row][col] = self.id
                elif row == 7 and col == 3:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_queen)
                    self.images_list[row][col] = self.id
                elif row == 7 and col == 4:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_king)
                    self.images_list[row][col] = self.id

            # reset position x,y
            x = 0
            y = 0

    def ischecked(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        self.update_temporary(old_color, old_name, new_row, new_col)
        for i in range(8):
            for j in range(8):
                check_list = self.list_moves(
                    self, old_row, old_col, old_color, old_name
                )
                if self.wk_location in check_list:
                    self.white_checked = True
                    return True

        self.return_update(old_color, old_name, new_row, new_col)
        self.white_checked = False
        return False

        # if old_color == "white":
        #     self.kr = self.wk_location[0]
        #     self.kc = self.wk_location[1]
        #     self.br = 0
        #     self.bc = 0
        #     for i in range(8):
        #         for j in range(8):
        #             if (i == self.kr or j == self.kc) and self.pieces_list[i][
        #                 j
        #             ].return_color() == "black":
        #                 self.white_checked = True
        #             elif (
        #                 abs(i - self.kr) == abs(j - self.kc)
        #                 and self.pieces_list[i][j].return_color() == "black"
        #             ):
        #                 self.white_checked = True
        #             elif (
        #                 i == self.kr - 2
        #                 and (j == self.kc - 1 or j == self.kc + 1)
        #                 and self.pieces_list[i][j].return_color() == "black"
        #             ):
        #                 self.white_checked = True
        #
        #             elif (
        #                 i == self.kr + 2
        #                 and (j == self.kc - 1 or j == self.kc + 1)
        #                 and self.pieces_list[i][j].return_color() == "black"
        #             ):
        #                 self.white_checked = True
        #
        #             elif (
        #                 i == self.kr - 1
        #                 and (j == self.kc - 2 or j == self.kc + 2)
        #                 and self.pieces_list[i][j].return_color() == "black"
        #             ):
        #                 self.white_checked = True
        #
        #             elif (
        #                 i == self.kr + 1
        #                 and (j == self.kc - 2 or j == self.kc + 2)
        #                 and self.pieces_list[i][j].return_color() == "black"
        #             ):
        #                 self.white_checked = True

    def return_update(self, old_color, old_name, new_row, new_col):
        """Return after update temporary piece."""
        self.pieces_list[old_row][old_col] = Piece(old_color, old_name)
        self.pieces_list[new_row][new_col] = Piece("none", "empty")
        Piece(old_color, old_name)

    def list_moves(self, old_row, old_col, old_color, old_name):
        ml = []

        for i in range(8):
            for j in range(8):
                new_color = self.pieces_list[i][j].return_color()
                new_name = self.pieces_list[i][j].return_name()
                # check if you chose empty case
                if old_name != "empty" and old_color != new_color:
                    if old_name == "pawn":
                        if self.check_pawn(
                            old_row,
                            old_col,
                            i,
                            j,
                            old_color,
                            old_name,
                            new_color,
                            new_name,
                        ):
                            ml.append((i, j))

                    elif old_name == "rook":
                        if self.check_rook(
                            old_row,
                            old_col,
                            i,
                            j,
                            old_color,
                            old_name,
                            new_color,
                            new_name,
                        ):
                            ml.append((i, j))

                    elif old_name == "knight":
                        if self.check_knight(
                            old_row,
                            old_col,
                            i,
                            j,
                            old_color,
                            old_name,
                            new_color,
                            new_name,
                        ):
                            ml.append((i, j))

                    elif old_name == "bishop":
                        if self.check_bishop(
                            old_row,
                            old_col,
                            i,
                            j,
                            old_color,
                            old_name,
                            new_color,
                            new_name,
                        ):
                            ml.append((i, j))

                    elif old_name == "queen":
                        if self.check_queen(
                            old_row,
                            old_col,
                            i,
                            j,
                            old_color,
                            old_name,
                            new_color,
                            new_name,
                        ):
                            ml.append((i, j))
        return ml

    def update_temporary(self, old_color, old_name, new_row, new_col):
        """Update temporary piece."""
        self.pieces_list[old_row][old_col] = Piece("none", "empty")
        x = (SIZE * (new_col + 1)) + 8
        y = (SIZE * (new_row + 1)) + 8
        self.pieces_list[new_row][new_col] = Piece(old_color, old_name)

    def return_turn(self):
        """Return turn for class Chess."""
        return self.turn

    def change_turn(self):
        """Change turn of player."""
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def remove(self, canvas, old_row, old_col, new_row, new_col, new_name):
        """Remove piece."""
        canvas.delete(self.images_list[old_row][old_col])
        self.images_list[old_row][old_col] = "None"
        self.pieces_list[old_row][old_col] = Piece("none", "empty")
        if new_name != "empty":
            canvas.delete(self.images_list[new_row][new_col])
            self.images_list[new_row][new_col] = "None"

    def update_move(self, canvas, image, old_color, old_name, new_row, new_col):
        """Reset piece."""
        x = (SIZE * (new_col + 1)) + 8
        y = (SIZE * (new_row + 1)) + 8
        self.id = canvas.create_image(x, y, anchor=NW, image=image)
        self.images_list[new_row][new_col] = self.id
        self.pieces_list[new_row][new_col] = Piece(old_color, old_name)
        # self.update_count()

    def check_legal(self, canvas, old_row, old_col, new_row, new_col):
        """Check if move is legal."""

        self.old_name = self.pieces_list[old_row][old_col].return_name()
        self.new_name = self.pieces_list[new_row][new_col].return_name()
        self.old_color = self.pieces_list[old_row][old_col].return_color()
        self.new_color = self.pieces_list[new_row][new_col].return_color()

        # check if your turn
        if (self.turn == 0 and self.old_color == "black") or (
            self.turn == 1 and self.old_color == "white"
        ):
            return False
        # check if you chose empty case
        if self.old_name == "empty":
            return False
        # check if you attack your team
        if self.old_color == self.new_color:
            return False

        # Check
        if ischecked(
            old_row,
            old_col,
            new_row,
            new_col,
            self.old_color,
            self.old_name,
            self.new_color,
            self.new_name,
        ):
            return False

        if self.old_name == "pawn":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_pawn(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_pawn
                else:
                    self.image = self.b_pawn
                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()

                return True
        elif self.old_name == "king":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_king(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_king
                    self.wk_location[0] = new_row
                    self.wk_location[1] = new_col
                else:
                    self.image = self.b_king
                    self.bk_location[0] = new_row
                    self.bk_location[1] = new_col

                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()
                print(self.turn)
                return True

        elif self.old_name == "rook":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_rook(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_rook
                else:
                    self.image = self.b_rook
                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()
                print(self.turn)

                return True

        elif self.old_name == "bishop":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_bishop(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_bishop
                else:
                    self.image = self.b_bishop
                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()
                print(self.turn)
                return True

        elif self.old_name == "queen":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_queen(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_queen
                else:
                    self.image = self.b_queen
                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()
                print(self.turn)
                return True
        elif self.old_name == "knight":
            print(self.list_moves(old_row, old_col, self.old_color, self.old_name))
            if self.check_knight(
                old_row,
                old_col,
                new_row,
                new_col,
                self.old_color,
                self.old_name,
                self.new_color,
                self.new_name,
            ):
                self.remove(
                    canvas,
                    old_row,
                    old_col,
                    new_row,
                    new_col,
                    self.new_name,
                )
                if self.old_color == "white":
                    self.image = self.w_knight
                else:
                    self.image = self.b_knight
                self.update_move(
                    canvas, self.image, self.old_color, self.old_name, new_row, new_col
                )
                self.change_turn()
                print(self.turn)
                return True

        return False

    def check_pawn(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of pawn is legal."""

        if old_color == "white":
            if new_name == "empty" and old_col == new_col:
                if old_row == new_row + 1:
                    return True
                elif old_row == new_row + 2 and old_row == 6:
                    for i in range(old_row - 1, new_row, -1):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                    return True

            elif new_name != "empty" and old_row == new_row + 1:
                if old_col == new_col:
                    return True
                elif old_col == new_col + 1 or old_col == new_col - 1:
                    return True

            else:
                return False

        if old_color == "black":
            if new_name == "empty" and old_col == new_col:
                if old_row == new_row - 1:
                    return True
                elif old_row == new_row - 2 and old_row == 1:
                    for i in range(old_row + 1, new_row):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                    return True

            elif new_name != "empty" and old_row == new_row - 1:
                if old_col == new_col:
                    return True
                elif old_col == new_col + 1 or old_col == new_col - 1:
                    return True
            else:
                return False

    def check_king(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of king is legal."""

        if old_col == new_col:
            if (old_row == new_row + 1) or (old_row == new_row - 1):
                return True
        elif (old_col == new_col + 1) or (old_col == new_col - 1):
            if old_row == new_row:
                return True
            elif (old_row == new_row + 1) or (old_row == new_row - 1):
                return True
        else:
            return False

    def check_rook(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of rook is legal."""
        if old_row == new_row:
            # move to right
            if old_col < new_col:
                if old_col == new_col + 1:
                    return True
                else:
                    for i in range(old_col + 1, new_col):
                        if self.pieces_list[old_row][i].return_name() != "empty":
                            return False
                return True
            # move to left
            elif old_col > new_col:
                if old_col == new_col + 1:
                    return True
                else:
                    for i in range(old_col - 1, new_col, -1):
                        if self.pieces_list[old_row][i].return_name() != "empty":
                            return False
                return True

        elif old_col == new_col:
            # move up
            if old_row > new_row:
                if old_row == new_row + 1:
                    return True
                else:
                    for i in range(old_row - 1, new_row, -1):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                return True
            # move down
            if old_row < new_row:
                if old_row == new_row - 1:
                    return True
                else:
                    for i in range(old_row + 1, new_row):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                return True
        else:
            return False

    def check_bishop(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of bishop is legal."""
        # the absolute value for check diagonal
        self.absolute_row = abs(old_row - new_row)
        self.absolute_col = abs(old_col - new_col)

        # move to up right
        if (old_row > new_row) and (old_col < new_col):
            if (old_row == new_row + 1) and (old_col == new_col - 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col + 1, new_col):
                    old_row -= 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False
        # move to up left
        if (old_row > new_row) and (old_col > new_col):
            if (old_row == new_row + 1) and (old_col == new_col + 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col - 1, new_col, -1):
                    old_row -= 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        # move to down right
        if (old_row < new_row) and (old_col < new_col):
            if (old_row == new_row - 1) and (old_col == new_col - 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col + 1, new_col):
                    old_row += 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        # move to left right
        if (old_row < new_row) and (old_col > new_col):
            if (old_row == new_row - 1) and (old_col == new_col + 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                print("enter")
                for i in range(old_col - 1, new_col, -1):

                    old_row += 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        else:
            return False

    def check_knight(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of knight is legal."""

        if (old_row == new_row + 2) or (old_row == new_row - 2):
            if (old_col == new_col + 1) or (old_col == new_col - 1):
                return True
        elif (old_col == new_col + 2) or (old_col == new_col - 2):
            if (old_row == new_row + 1) or (old_row == new_row - 1):
                return True
        else:
            return False

    def check_queen(
        self,
        old_row,
        old_col,
        new_row,
        new_col,
        old_color,
        old_name,
        new_color,
        new_name,
    ):
        """Check if move of queen is legal."""
        if old_row == new_row:
            # move to right
            if old_col < new_col:
                if old_col == new_col + 1:
                    return True
                else:
                    for i in range(old_col + 1, new_col):
                        if self.pieces_list[old_row][i].return_name() != "empty":
                            return False

            # move to left
            elif old_col > new_col:
                if old_col == new_col + 1:
                    return True
                else:
                    for i in range(old_col - 1, new_col, -1):
                        if self.pieces_list[old_row][i].return_name() != "empty":
                            return False
                return True

        elif old_col == new_col:
            # move up
            if old_row > new_row:
                if old_row == new_row + 1:
                    return True
                else:
                    for i in range(old_row - 1, new_row, -1):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                    return True
            # move down
            if old_row < new_row:
                if old_row == new_row - 1:
                    return True
                else:
                    for i in range(old_row + 1, new_row):
                        if self.pieces_list[i][old_col].return_name() != "empty":
                            return False
                    return True

        # move to up right
        elif (old_row > new_row) and (old_col < new_col):
            if (old_row == new_row + 1) and (old_col == new_col - 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col + 1, new_col):
                    old_row -= 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False
        # move to up left
        elif (old_row > new_row) and (old_col > new_col):
            if (old_row == new_row + 1) and (old_col == new_col + 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col - 1, new_col, -1):
                    old_row -= 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        # move to down right
        elif (old_row < new_row) and (old_col < new_col):
            if (old_row == new_row - 1) and (old_col == new_col - 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                for i in range(old_col + 1, new_col):
                    old_row += 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        # move to left right
        elif (old_row < new_row) and (old_col > new_col):
            if (old_row == new_row - 1) and (old_col == new_col + 1):
                return True
            # check diagonal
            elif self.absolute_row == self.absolute_col:
                print("enter")
                for i in range(old_col - 1, new_col, -1):

                    old_row += 1
                    if self.pieces_list[old_row][i].return_name() != "empty":
                        return False
                return True
            else:
                return False

        else:
            return False


class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def return_name(self):
        return self.name

    def return_color(self):
        return self.color


# #****************************************************************
class Game:
    """Class pour mettre en lien tous les autres class."""

    def __init__(self, frame):
        """Définir les bases de game et appeler les autres méthodes."""
        width = 1024
        height = 1024
        self.frame = frame
        self.turn = 0
        # self.sec = 0
        self.white_count = 0
        self.black_count = 0
        self.canvas = tk.Canvas(self.frame, width=width, height=height)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.ecran = tk.PhotoImage(file="w2.png")
        self.board = Board(width, height)
        self.coordination = coordination
        self.valid_case = valid_case
        self.lbl = tk.Label(self.frame, text="")
        # Clock for White
        self.time_white = tk.Label(
            self.frame, text="Timer for White:", font=("Arial", 20)
        ).place(x=670, y=10)
        self.wc = StringVar()
        self.wc.set("00:00:00")
        self.wlb = Label(
            self.frame, textvariable=self.wc, font=("Arial", 20), bg="white"
        ).place(x=900, y=10)

        # Clock for Black
        self.time_black = tk.Label(
            self.frame, text="Timer for Black:", font=("Arial", 20)
        ).place(x=670, y=60)
        self.bc = StringVar()
        self.bc.set("00:00:00")
        self.blb = Label(
            self.frame, textvariable=self.bc, font=("Arial", 20), bg="white"
        ).place(x=900, y=50)
        # self.time_info = tk.Label(
        #     self.frame, text="You are 300s of your turn!", font=("Arial", 20)
        # ).place(x=670, y=10)
        # self.time = tk.Label(self.frame, text="Timer", font=("Arial", 20)).place(
        #     x=670, y=50
        # )
        # self.displaytime = tk.Label(text="", font=("Arial", 20), fg="black")
        # self.displaytime.place(x=770, y=50)

        # display turn of player
        self.my_var = StringVar()
        self.my_var.set("It's turn of White!")
        self.displayturn1 = tk.Label(
            self.frame, textvariable=self.my_var, font=("Arial", 25)
        )
        self.displayturn1.place(x=720, y=100)

        # move
        self.displayturn2 = tk.Label(
            self.frame, text="Please chose your piece!", font=("Arial", 25)
        ).place(x=100, y=680)
        self.from_label = tk.Label(self.frame, text="From", font=("Arial", 15)).place(
            x=30, y=750
        )
        self.to_label = tk.Label(self.frame, text="To", font=("Arial", 15)).place(
            x=250, y=750
        )

        # # TextBox Creation
        self.player_input1 = tk.Entry(self.frame, font=("Arial", 18))
        self.player_input1.place(x=100, y=750, height=30, width=100)

        self.player_input2 = tk.Entry(self.frame, font=("Arial", 18))
        self.player_input2.place(x=300, y=750, height=30, width=100)

        # Button Creation
        self.btn = tk.Button(
            self.frame, text="Ok", font=("Arial", 15), command=lambda: self.get_move()
        ).place(x=450, y=750, height=30, width=100)

        # clock
        # self.update_clock()
        self.start_whiteclock()

    def start(self):
        """Create background and install chessboard and pieces."""
        self.canvas.create_image(0, 0, image=self.ecran, tags="image", anchor="nw")
        self.board.install_in(self.canvas)
        self.board.install_pieces(self.canvas)

    def start_animation(self):
        """Appeler la création des bases au méthode start()."""
        self.start()

    def start_whiteclock(self):
        """Start or reset clock of White."""
        self.white_count = 0
        self.white_timer()

    def stop_whiteclock(self):
        """Stop clock of White."""
        self.white_count = 1

    def start_blackclock(self):
        """Start or reset clock of White."""
        self.black_count = 0
        self.black_timer()

    def stop_blackclock(self):
        """Stop clock of White."""
        self.black_count = 1

    def white_timer(self):
        """Time calculator of White."""
        if self.white_count == 0:
            self.d = str(self.wc.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.wc.set(self.d)
            self.frame.after(1000, self.white_timer)

    def black_timer(self):
        """Time calculator of Black."""
        if self.black_count == 0:
            self.d = str(self.bc.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.bc.set(self.d)
            self.frame.after(1000, self.black_timer)

    # find index of row and column
    def find_indexcase(self, element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return i, j

    # def update_clock(self):
    #     """Mettre à jour le temps."""
    #     self.sec = self.sec + 1
    #     self.displaytime.configure(text=self.sec)
    #     self.canvas.after(1000, self.update_clock)
    #     while self.sec == 300:
    #         self.sec = 0

    # update and display turn of player!
    def update_turn(self):
        if self.turn == 1:
            self.my_var.set("Turn of Black")
        else:
            self.my_var.set("Turn of White")
        # print("inupdate", self.turn)

    def get_move(self):
        self.value_from = self.player_input1.get().upper()
        self.value_to = self.player_input2.get().upper()

        print(self.turn)
        print(self.value_from, self.value_to)

        if (self.value_from in self.valid_case) and (self.value_to in self.valid_case):

            self.lbl.config(text="Provided Input: " + self.value_from + self.value_to)
            self.lbl.place(x=450, y=900, height=30, width=100)

            self.old_row, self.old_col = self.find_indexcase(
                self.value_from, self.coordination
            )
            self.new_row, self.new_col = self.find_indexcase(
                self.value_to, self.coordination
            )

            if self.board.check_legal(
                self.canvas, self.old_row, self.old_col, self.new_row, self.new_col
            ):
                self.turn = self.board.return_turn()
                if self.turn == 1:
                    self.stop_whiteclock()
                    self.start_blackclock()
                else:
                    self.stop_blackclock()
                    self.start_whiteclock()
                self.update_turn()

            else:
                messagebox.showerror(
                    "Error MessageBox", "An illegal move! Please make a legal move!"
                )
        else:
            messagebox.showwarning(
                "Warning MessageBox", "Please enter valid case name!"
            )


class Chess:
    """Main Game class."""

    def __init__(self):
        """Création frame et titre du jeu."""
        self.root = tk.Tk()
        self.root.title("Chess game")
        self.frame = tk.Frame(self.root, width=1024, height=1024)
        self.frame.pack()

        # self.w = tk.Label(self.frame, text="Hello Tkinter!")
        # self.w.place(x=800, y=100)
        # self.w.pack()

        # self.root.mainloop()

        self.game = Game(self.frame)

    def play(self):
        """Méthode pour commmencer le jeu."""
        self.game.start_animation()
        self.root.mainloop()


if __name__ == "__main__":

    jeux = Chess()
    jeux.play()
