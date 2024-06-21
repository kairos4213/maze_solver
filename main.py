from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    cell_one = Cell(50, 100, 100, 150, win, left_wall=False, bottom_wall=False)
    cell_two = Cell(50, 100, 150, 200, win, top_wall=False, bottom_wall=False)
    cell_three = Cell(50, 100, 200, 250, win, top_wall=False, right_wall=False)
    cell_four = Cell(100, 150, 200, 250, win, left_wall=False, right_wall=False)

    cell_one.draw()
    cell_two.draw()
    cell_three.draw()
    cell_four.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
