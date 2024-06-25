import time
import random

from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols

        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        maze_entrance = self._cells[0][0]
        maze_exit = self._cells[-1][-1]

        maze_entrance.has_top_wall = False
        maze_exit.has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(len(self._cells) - 1, len(self._cells[-1]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            current_cell = self._cells[i][j]
            move_direction = random.randrange(len(to_visit))
            next_cell_index = to_visit[move_direction]
            if next_cell_index[0] == i - 1:
                current_cell.has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_cell_index[0] == i + 1:
                current_cell.has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_cell_index[1] == j - 1:
                current_cell.has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            if next_cell_index[1] == j + 1:
                current_cell.has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_cell_index[0], next_cell_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        self._animate()
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            return True

        # Check right neighbor
        if (
            i < self._num_cols - 1
            and self._cells[i + 1][j]
            and not self._cells[i + 1][j].has_left_wall
            and not self._cells[i + 1][j].visited
        ):
            current_cell.draw_move(self._cells[i + 1][j])
            check_cell = self._solve_r(i + 1, j)
            if check_cell:
                return True
            else:
                current_cell.draw_move(self._cells[i + 1][j], True)

        # Check left neighbor
        if (
            i > 0
            and self._cells[i - 1][j]
            and not self._cells[i - 1][j].has_right_wall
            and not self._cells[i - 1][j].visited
        ):
            current_cell.draw_move(self._cells[i - 1][j])
            check_cell = self._solve_r(i - 1, j)
            if check_cell:
                return True
            else:
                current_cell.draw_move(self._cells[i - 1][j], True)

        # Check top neighbor
        if (
            j > 0
            and self._cells[i][j - 1]
            and not self._cells[i][j - 1].has_bottom_wall
            and not self._cells[i][j - 1].visited
        ):
            current_cell.draw_move(self._cells[i][j - 1])
            check_cell = self._solve_r(i, j - 1)
            if check_cell:
                return True
            else:
                current_cell.draw_move(self._cells[i][j - 1], True)

        # Check bottom neighbor
        if (
            j < self._num_rows - 1
            and self._cells[i][j + 1]
            and not self._cells[i][j + 1].has_top_wall
            and not self._cells[i][j + 1].visited
        ):
            current_cell.draw_move(self._cells[i][j + 1])
            check_cell = self._solve_r(i, j + 1)
            if check_cell:
                return True
            else:
                current_cell.draw_move(self._cells[i][j + 1], True)

        return False
