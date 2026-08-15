import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("800x600")

pen_color = "black"
brush_size = 3

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(
        x - brush_size,
        y - brush_size,
        x + brush_size,
        y + brush_size,
        fill=pen_color,
        outline=pen_color
    )

def choose_color():
    global pen_color
    color = colorchooser.askcolor()[1]
    if color:
        pen_color = color

def use_eraser():
    global pen_color
    pen_color = "white"

def clear_canvas():
    canvas.delete("all")

def change_size(value):
    global brush_size
    brush_size = int(value)
    
top_frame = tk.Frame(root)
top_frame.pack(fill="x")

color_btn = tk.Button(top_frame, text="Choose Color", command=choose_color)
color_btn.pack(side="left", padx=5, pady=5)

eraser_btn = tk.Button(top_frame, text="Eraser", command=use_eraser)
eraser_btn.pack(side="left", padx=5)

clear_btn = tk.Button(top_frame, text="Clear", command=clear_canvas)
clear_btn.pack(side="left", padx=5)

size_scale = tk.Scale(
    top_frame,
    from_=1,
    to=20,
    orient="horizontal",
    label="Brush Size",
    command=change_size
)
size_scale.set(3)
size_scale.pack(side="left", padx=10)

canvas = tk.Canvas(root, bg="white", width=800, height=550)
canvas.pack(fill="both", expand=True)

canvas.bind("<B1-Motion>", draw)

root.mainloop()