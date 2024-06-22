from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(250, 150, 5, 5, 50, 50, win)
    maze._break_entrance_and_exit()

    win.wait_for_close()


if __name__ == "__main__":
    main()
