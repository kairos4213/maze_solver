from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Maze Solver")

        self.canvas = Canvas(self.root, self.width, self.height)
        self.canvas.pack()

        self.running = False
