import unittest
from Tests import ToolsForTesting as TFT
from Pathfinders import GoTo

level_map = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


class TestPathfinders(unittest.TestCase):

    def setUp(self):
        self.go_to = GoTo()
        self.start = (2, 2)
        self.end = (5, 5)

    def test_goto_no_obstacles(self):
        found_path = self.go_to.find_path(level_map, self.start, self.end)
        self.assertEqual(len(found_path), 2)
        for position in found_path:
            self.assertLess(TFT.calculate_manhattan_distance(position, self.end),
                            TFT.calculate_manhattan_distance(self.start, self.end))

    def test_goto_obstacle(self):
        pass

    def test_goto_no_valid_path(self):
        pass


if __name__ == "__main__":
    unittest.main()