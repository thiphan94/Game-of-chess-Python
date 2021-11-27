"""Chess game."""

import time
import math
import random
import json
import operator
import numpy as np


from matrix import board_name, coordination, board_coordination

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

SIZE = 64
from tkinter import *


class Board:
    def __init__(self, height, width, color="#815426"):
        self.height = height
        self.width = width
        self.color = color
        self.turn = 0
        self.first_move = 1
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
        self.image = tk.PhotoImage(file="img/w_pawn.png")
        # list for stockage pieces
        self.piece_list = [
            [Piece("none", "empty") for col in range(8)] for row in range(8)
        ]
        self.images_list = [[[None] for col in range(8)] for row in range(8)]

        self.id = None
        self.coordination = coordination
        self.b_name = board_name

        self.create_list()
        # self.image = tk.PhotoImage(file="img/b_pawn.png")

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

        # print(self.board_initial)

    def create_list(self):
        for row in range(8):
            for col in range(8):

                if row == 1:
                    self.piece_list[row][col] = Piece("black", "pawn")
                elif row == 6:
                    self.piece_list[row][col] = Piece("white", "pawn")
                elif (row == 0 and col == 0) or (row == 0 and col == 7):
                    self.piece_list[row][col] = Piece("black", "rook")
                elif (row == 0 and col == 1) or (row == 0 and col == 6):
                    self.piece_list[row][col] = Piece("black", "knight")
                elif (row == 0 and col == 2) or (row == 0 and col == 5):
                    self.piece_list[row][col] = Piece("black", "bishop")
                elif row == 0 and col == 3:
                    self.piece_list[row][col] = Piece("black", "queen")
                elif row == 0 and col == 4:
                    self.piece_list[row][col] = Piece("black", "king")
                elif (row == 7 and col == 0) or (row == 7 and col == 7):
                    self.piece_list[row][col] = Piece("white", "rook")
                elif (row == 7 and col == 1) or (row == 7 and col == 6):
                    self.piece_list[row][col] = Piece("white", "knight")
                elif (row == 7 and col == 2) or (row == 7 and col == 5):
                    self.piece_list[row][col] = Piece("white", "bishop")
                elif row == 7 and col == 3:
                    self.piece_list[row][col] = Piece("white", "queen")
                elif row == 7 and col == 4:
                    self.piece_list[row][col] = Piece("white", "king")
                else:
                    self.piece_list[row][col] = Piece("none", "empty")

    def install_pieces(self, canvas):
        """set up pieces."""
        # canvas.create_image(0, 0, anchor=NW, image=self.w_pawn)
        self.images = list()
        for row in range(8):
            y = (SIZE * (row + 1)) + 8
            new = []
            for col in range(8):
                x = (SIZE * (col + 1)) + 8
                if row == 1:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_pawn)
                    new.append(self.id)
                elif row == 6:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_pawn)
                    new.append(self.id)
                elif (row == 0 and col == 0) or (row == 0 and col == 7):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_rook)
                    new.append(self.id)
                elif (row == 0 and col == 1) or (row == 0 and col == 6):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_knight)
                    new.append(self.id)
                elif (row == 0 and col == 2) or (row == 0 and col == 5):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_bishop)
                    new.append(self.id)
                elif row == 0 and col == 3:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_queen)
                    new.append(self.id)
                elif row == 0 and col == 4:
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.b_king)
                elif (row == 7 and col == 0) or (row == 7 and col == 7):
                    new.append(self.id)
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_rook)
                    new.append(self.id)
                elif (row == 7 and col == 1) or (row == 7 and col == 6):
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_knight)
                    new.append(self.id)
                elif (row == 7 and col == 2) or (row == 7 and col == 5):
                    canvas.create_image(x, y, anchor=NW, image=self.w_bishop)
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_bishop)
                    new.append(self.id)
                elif row == 7 and col == 3:
                    canvas.create_image(x, y, anchor=NW, image=self.w_queen)
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_queen)
                    new.append(self.id)
                elif row == 7 and col == 4:
                    canvas.create_image(x, y, anchor=NW, image=self.w_king)
                    self.id = canvas.create_image(x, y, anchor=NW, image=self.w_king)
                    new.append(self.id)
                else:
                    new.append("Empty")
            # reset position x,y
            x = 0
            y = 0
            self.images_list.append(new)

        # print(self.piece_list)

    def remove(self, canvas):
        canvas.delete(self.piece_list[1][0])

    def reset(self, canvas):
        pass

    def check_legal(self, old_row, old_col, new_row, new_col):
        print(old_row, old_col, new_row, new_col)
        self.old_name = self.piece_list[old_row][old_col].return_name()
        self.new_name = self.piece_list[new_row][new_col].return_name()
        self.old_color = self.piece_list[old_row][old_col].return_color()
        self.new_color = self.piece_list[new_row][new_col].return_color()

        print(self.old_color, self.old_name)
        print(self.new_color, self.new_name)

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

        if self.old_name == "pawn":
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
                return True

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
        if old_color == "white":
            if new_name == "empty" and old_col == new_col:
                if old_row == new_row + 1:
                    return True
                if old_row == new_row + 2 and old_row == 6:
                    return True

            elif new_name != "empty" and old_row == new_row + 1:
                if old_col == new_col:
                    return True
                elif old_col == new_col + 1 or old_col == new_col - 1:
                    return True

        if old_color == "black":
            if new_name == "empty" and old_col == new_col:
                if old_row == new_row - 1:
                    return True
                if old_row == new_row - 2 and old_row == 1:
                    return True

            elif new_name != "empty" and old_row == new_row - 1:
                if old_col == new_col:
                    return True
                elif old_col == new_col + 1 or old_col == new_col - 1:
                    return True


# class Piece:
#     def __init__(self, color, type, canvas,x,y):
#         # self.height = height
#         # self.width = width
#         self.color = color
#         self.type = type
#         self.canvas = canvas


class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    # def set_image(self):
    #     if self.color == "white":
    #         file_name = "img/" + "w_" + self.name + ".png"
    #     else:
    #         file_name = "img/" + "b_" + self.name + ".png"
    #     return file_name

    def return_name(self):
        return self.name

    def return_color(self):
        return self.color


# class Rook(Piece):
#     def __init__(self, color, type, canvas, x, y):
#         super().__init__(color, type, canvas)
#         if color == "white":
#             file_name = "img/" + "w_" + type + ".png"
#         else:
#             file_name = "img/" + "b_" + type + ".png"
#         # print(file_name)
#         self.title = tk.PhotoImage(file=file_name)
#         canvas.create_image(x, y, anchor=NW, image=self.title)
#
#
# class Knight(Piece):
#     def __init__(self, color, type, canvas, x, y):
#         super().__init__(color, type, canvas)
#         if color == "white":
#             file_name = "img/" + "w_" + type + ".png"
#         else:
#             file_name = "img/" + "b_" + type + ".png"
#         # print(file_name)
#         self.title = tk.PhotoImage(file=file_name)
#         canvas.create_image(x, y, anchor=NW, image=self.title)
#
#
# class Bishop(Piece):
#     def __init__(self, color, type, canvas, x, y):
#         super().__init__(color, type, canvas)
#         if color == "white":
#             file_name = "img/" + "w_" + type + ".png"
#         else:
#             file_name = "img/" + "b_" + type + ".png"
#         # print(file_name)
#         self.title = tk.PhotoImage(file=file_name)
#         canvas.create_image(x, y, anchor=NW, image=self.title)
#
#
# class Queen(Piece):
#     def __init__(self, color, type, canvas, x, y):
#         super().__init__(color, type, canvas)
#         if color == "white":
#             file_name = "img/" + "w_" + type + ".png"
#         else:
#             file_name = "img/" + "b_" + type + ".png"
#         # print(file_name)
#         self.title = tk.PhotoImage(file=file_name)
#         canvas.create_image(x, y, anchor=NW, image=self.title)
#
#
# class King(Piece):
#     def __init__(self, color, type, canvas, x, y):
#         super().__init__(color, type, canvas)
#         if color == "white":
#             file_name = "img/" + "w_" + type + ".png"
#         else:
#             file_name = "img/" + "b_" + type + ".png"
#         self.title = tk.PhotoImage(file=file_name)
#         canvas.create_image(x, y, anchor=NW, image=self.title)
#

# #****************************************************************
class Game:
    """Class pour mettre en lien tous les autres class."""

    def __init__(self, frame):
        """Définir les bases de game et appeler les autres méthodes."""
        width = 1024
        height = 1024
        self.frame = frame
        self.turn = 0
        self.canvas = tk.Canvas(self.frame, width=width, height=height)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.ecran = tk.PhotoImage(file="w2.png")
        self.board = Board(width, height)
        self.coordination = coordination
        self.matrix = board_name

        self.lbl = tk.Label(self.frame, text="")
        self.displayturn1 = tk.Label(
            self.frame, text="Turn of {0}".format(self.turn), font=("Arial", 25)
        ).place(x=720, y=100)

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

    def start(self):
        """Commencer à créer défender, aliens, bunkers."""
        self.canvas.create_image(0, 0, image=self.ecran, tags="image", anchor="nw")

        self.board.install_in(self.canvas)
        self.board.install_pieces(self.canvas)

        # self.pieces.install_in(self.canvas)
        # self.pieces.remove(self.canvas)

    def start_animation(self):
        """Appeler la création des bases au méthode start()."""
        self.start()

    def find_indexcase(self, element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return i, j

    def get_move(self):
        self.value_from = self.player_input1.get()
        self.value_to = self.player_input2.get()
        self.lbl.config(text="Provided Input: " + self.value_from + self.value_to)
        self.lbl.place(x=450, y=900, height=30, width=100)

        self.old_row, self.old_col = self.find_indexcase(
            self.value_from, self.coordination
        )
        self.new_row, self.new_col = self.find_indexcase(
            self.value_to, self.coordination
        )

        if self.board.check_legal(
            self.old_row, self.old_col, self.new_row, self.new_col
        ):
            print("ok")


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
