from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall, c.has_right_wall = False, False
    c.draw(100, 100, 125, 125)

    c2 = Cell(win)
    c2.has_left_wall, c2.has_bottom_wall = False, False
    c2.draw(125, 100, 150, 125)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(125, 125, 175, 150)

    c.draw_move(c2)
    c2.draw_move(c3, True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
