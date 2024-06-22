import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_wide_maze(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_tall_maze(self):
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_small_maze(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_large_maze(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_entrance_exit_walls_removed(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()

        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()