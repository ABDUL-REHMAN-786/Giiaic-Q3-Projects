# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
# We then create an eraser rectangle which, when dragged around the canvas, 
# sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Constants
CANVAS_SIZE = 400
CELL_SIZE = 40
ERASER_SIZE = 50

class EraserCanvas:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white")
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = {}  # Store cell references
        for row in range(0, CANVAS_SIZE, CELL_SIZE):
            for col in range(0, CANVAS_SIZE, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells[(col, row)] = cell  # Store cell references

        # Create the eraser (draggable rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")

        # Bind mouse events for dragging
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        """Move eraser and erase any cells it touches."""
        x1, y1 = event.x, event.y
        x2, y2 = x1 + ERASER_SIZE, y1 + ERASER_SIZE

        # Move the eraser
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check for collision with cells and erase them
        for (col, row), cell in self.cells.items():
            if self.is_eraser_touching(col, row):
                self.canvas.itemconfig(cell, fill="white")  # Change cell color to white

    def is_eraser_touching(self, col, row):
        """Check if the eraser is touching a cell."""
        x1, y1, x2, y2 = self.canvas.coords(self.eraser)
        return (col < x2 and col + CELL_SIZE > x1 and
                row < y2 and row + CELL_SIZE > y1)

# Run the application
root = tk.Tk()
root.title("Eraser Tool on Canvas")
app = EraserCanvas(root)
root.mainloop()
# The code creates a simple GUI application using Tkinter that simulates an eraser tool on a canvas.
# The canvas is filled with blue rectangles representing cells, and a gray rectangle serves as the eraser.