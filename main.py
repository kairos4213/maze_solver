from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 8, 8, 50, 50, win, 8)

    win.wait_for_close()


if __name__ == "__main__":
    main()
