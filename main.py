from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall, c.has_right_wall = False, False
    c.draw(100, 100, 125, 125)

    c = Cell(win)
    c.has_left_wall, c.has_bottom_wall = False, False
    c.draw(125, 100, 150, 125)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(125, 125, 175, 150)

    win.wait_for_close()


if __name__ == "__main__":
    main()
