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
    def __init__(self, height, width, color="#efe4d6"):
        self.height = height
        self.width = width
        self.color = color

    def install_in(self, canvas):
        """Création de chessboard."""
        for y in range(10):
            for x in range(10):
                x0 = x * SIZE
                y0 = y * SIZE
                x1 = x0 + SIZE
                y1 = y0 + SIZE
                # create border
                if y < 1 or y == 9 or x < 1 or x == 9:
                    canvas.create_rectangle((x0, y0, x1, y1), fill="#F8F8FF", width=0)
                else:
                    canvas.create_rectangle((x0, y0, x1, y1), fill=self.color)
                    if self.color == "#efe4d6":
                        self.color = "#815426"
                    else:
                        self.color = "#efe4d6"

            if self.color == "#efe4d6":
                self.color = "#815426"
            else:
                self.color = "#efe4d6"


class Pieces:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.image = tk.PhotoImage(file="img/b_bishop.png")

    def install_in(self, canvas):
        """Création de chessboard."""
        # Load an image in the script
        # img = ImageTk.PhotoImage(Image.open("img/b_bishop.png"))

        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=self.image)
        # white_list = ["w_rook", "w_knight", "w_bishop", "w_king", "w_queen", "w_pawn"]
        # black_list = ["b_rook", "b_knight", "b_bishop", "b_king", "b_queen", "b_pawn"]
        # for y in range(1, 10):
        #     for x in range(1, 10):
        #         # x0 = x * SIZE
        #         # y0 = y * SIZE
        #         # x1 = x0 + SIZE
        #         # y1 = y0 + SIZE
        #         # if y < 1 or y == 9 or x < 1 or x == 9:
        #         #     canvas.create_rectangle((x0, y0, x1, y1), fill="#F8F8FF", width=0)
        #         # else:
        #         # canvas.create_rectangle((x0, y0, x1, y1), fill=self.color)
        #         # load the .gif image file
        #
        #         if x == 1:
        #
        #             gif1 = PhotoImage(file="img/w_rook.png")
        #
        #             # put gif image on canvas
        #             # pic's upper left corner (NW) on the canvas is at x=50 y=10
        #             canvas.create_image(200, 200, image=gif1, anchor=NW)
        #


# SIZE = 96
#
# root = tk.Tk()
#
# canvas = tk.Canvas(root, height=1024, width=1024)
# canvas.pack()
#
# color = "#efe4d6"
#
# for y in range(8):
#
#     for x in range(8):
#         x0 = x * SIZE
#         y0 = y * SIZE
#         x1 = x0 + SIZE
#         y1 = y0 + SIZE
#         canvas.create_rectangle((x0, y0, x1, y1), fill=color)
#         if color == "#efe4d6":
#             color = "#815426"
#         else:
#             color = "#efe4d6"
#
#     if color == "#efe4d6":
#         color = "#815426"
#     else:
#         color = "#efe4d6"
#
#
# # load the .gif image file
# gif1 = PhotoImage(file="img/black_bishop.png")
#
# # put gif image on canvas
# # pic's upper left corner (NW) on the canvas is at x=50 y=10
# canvas.create_image(16, 16, image=gif1, anchor=NW)
#
# root.mainloop()
#

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
