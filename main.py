from window import Window, Point, Line


def main():
    win = Window(800, 600)

    top_line = Line(Point(200, 200), Point(500, 200))
    left_line = Line(Point(200, 200), Point(200, 500))
    right_line = Line(Point(500, 200), Point(500, 500))
    bottom_line = Line(Point(200, 500), Point(500, 500))

    win.draw_line(top_line, "green")
    win.draw_line(left_line, "green")
    win.draw_line(right_line, "green")
    win.draw_line(bottom_line, "green")

    win.wait_for_close()


if __name__ == "__main__":
    main()
