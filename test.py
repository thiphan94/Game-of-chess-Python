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

SIZE = 96

root = tk.Tk()

canvas = tk.Canvas(root, height=1024, width=1024)
canvas.pack()

color = "#815426"

for y in range(8):

    for x in range(8):
        x1 = x * SIZE
        y1 = y * SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == "#815426":
            color = "#efe4d6"
        else:
            color = "#815426"

    if color == "#815426":
        color = "#efe4d6"
    else:
        color = "#815426"


# load the .gif image file
gif1 = PhotoImage(file="img/b_bishop.png")

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(16, 16, image=gif1, anchor=NW)

img = PhotoImage(file="img/b_bishop.png")

# Add image to the Canvas Items
canvas.create_image(10, 10, anchor=NW, image=img)

root.mainloop()
