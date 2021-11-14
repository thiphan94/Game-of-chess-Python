import tkinter as tk
from tkinter import *

SIZE = 96

root = tk.Tk()

canvas = tk.Canvas(root, height=1024, width=1024)
canvas.pack()

color = "#efe4d6"

for y in range(8):

    for x in range(8):
        x1 = x * SIZE
        y1 = y * SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == "#efe4d6":
            color = "#815426"
        else:
            color = "#efe4d6"

    if color == "#efe4d6":
        color = "#815426"
    else:
        color = "#efe4d6"


# load the .gif image file
gif1 = PhotoImage(file="img/black_bishop.png")

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(16, 16, image=gif1, anchor=NW)

root.mainloop()
