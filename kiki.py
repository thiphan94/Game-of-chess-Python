import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
# frame.geometry("400x200")
# Function for getting Input
# from textbox and printing it
# at label widget


canvas = tk.Canvas(frame, width=500, height=200, bd=0, highlightthickness=0)
canvas.create_rectangle(245, 50, 345, 150, fill="black")
image = tk.PhotoImage(file="img/b_pawn.png")
image_id = canvas.create_image(50, 50, image=image)

canvas.move(image_id, 245, 100)

frame.mainloop()
