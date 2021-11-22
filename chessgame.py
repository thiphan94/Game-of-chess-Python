"""Chess game."""

import time
import math
import random
import json
import operator

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

# from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
SIZE = 64
from tkinter import *


class Board:
    def __init__(self, height, width, color="#815426"):
        self.height = height
        self.width = width
        self.color = color
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
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i1)
                    elif (col == 0 and row == 2) or (col == 9 and row == 2):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i2)
                    elif (col == 0 and row == 3) or (col == 9 and row == 3):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i3)
                    elif (col == 0 and row == 4) or (col == 9 and row == 4):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i4)
                    elif (col == 0 and row == 5) or (col == 9 and row == 5):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i5)
                    elif (col == 0 and row == 6) or (col == 9 and row == 6):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i6)
                    elif (col == 0 and row == 7) or (col == 9 and row == 7):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i7)
                    elif (col == 0 and row == 8) or (col == 9 and row == 8):
                        canvas.create_image(x0 + 16, y0 + 16, anchor=NW, image=self.i8)

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


class Pieces:
    def __init__(self, height, width):
        self.height = height
        self.width = width
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

    def install_in(self, canvas):
        """Création de chessboard."""
        # x = 72
        # y = 0

        black_list = ["b_rook", "b_knight", "b_bishop", "b_king", "b_queen", "b_pawn"]
        for row in range(8):
            y = (SIZE * (row + 1)) + 8
            for col in range(8):
                x = (SIZE * (col + 1)) + 8

                if row == 1:
                    canvas.create_image(x, y, anchor=NW, image=self.b_pawn)
                elif row == 6:
                    canvas.create_image(x, y, anchor=NW, image=self.w_pawn)
                elif (row == 0 and col == 0) or (row == 0 and col == 7):
                    canvas.create_image(x, y, anchor=NW, image=self.b_rook)
                elif (row == 0 and col == 1) or (row == 0 and col == 6):
                    canvas.create_image(x, y, anchor=NW, image=self.b_knight)
                elif (row == 0 and col == 2) or (row == 0 and col == 5):
                    canvas.create_image(x, y, anchor=NW, image=self.b_bishop)
                elif row == 0 and col == 3:
                    canvas.create_image(x, y, anchor=NW, image=self.b_queen)
                elif row == 0 and col == 4:
                    canvas.create_image(x, y, anchor=NW, image=self.b_king)
                elif (row == 7 and col == 0) or (row == 7 and col == 7):
                    canvas.create_image(x, y, anchor=NW, image=self.w_rook)
                elif (row == 7 and col == 1) or (row == 7 and col == 6):
                    canvas.create_image(x, y, anchor=NW, image=self.w_knight)
                elif (row == 7 and col == 2) or (row == 7 and col == 5):
                    canvas.create_image(x, y, anchor=NW, image=self.w_bishop)
                elif row == 7 and col == 3:
                    canvas.create_image(x, y, anchor=NW, image=self.w_queen)
                elif row == 7 and col == 4:
                    canvas.create_image(x, y, anchor=NW, image=self.w_king)

            x = 0
            y = 0


# #****************************************************************
class Game:
    """Class pour mettre en lien tous les autres class."""

    def __init__(self, frame):
        """Définir les bases de game et appeler les autres méthodes."""
        width = 1024
        height = 1024
        self.frame = frame
        self.canvas = tk.Canvas(self.frame, width=width, height=height)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.ecran = tk.PhotoImage(file="w2.png")
        self.board = Board(width, height)
        self.pieces = Pieces(width, height)

    def start(self):
        """Commencer à créer défender, aliens, bunkers."""
        self.canvas.create_image(0, 0, image=self.ecran, tags="image", anchor="nw")
        self.board.install_in(self.canvas)

        self.pieces.install_in(self.canvas)

        img = PhotoImage(file="img/b_bishop.png")

        # Add image to the Canvas Items
        self.canvas.create_image(10, 10, anchor=NW, image=img)

    def start_animation(self):
        """Appeler la création des bases au méthode start()."""
        self.start()


class Chess:
    """Main Game class."""

    def __init__(self):
        """Création frame et titre du jeu."""
        self.root = tk.Tk()
        self.root.title("Chess game")
        self.frame = tk.Frame(self.root, width=1024, height=1024)
        self.frame.pack()
        # self.root.mainloop()

        self.game = Game(self.frame)

    #
    def play(self):
        """Méthode pour commmencer le jeu."""
        self.game.start_animation()
        self.root.mainloop()


jeux = Chess()
jeux.play()

# if __name__ == "__main__":
