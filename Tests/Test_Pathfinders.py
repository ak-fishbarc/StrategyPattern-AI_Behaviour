import unittest
from Pathfinders import GoTo

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

level_map_with_obstacle = [[0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 0, 0]]

level_map_with_obstacle2 = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0],
                           [0, 0, 0, 5, 0]]


class TestPathfinders(unittest.TestCase):

    def setUp(self):
        self.go_to = GoTo()
        self.start = (2, 2)
        self.end = (2, 4)

    def test_goto_no_obstacles(self):
        found_path = self.go_to.find_path(level_map, self.start, self.end)
        self.assertGreater(len(found_path), 0)
        for position in found_path:
            self.assertLessEqual(self.go_to.calculate_euclidean_distance(position, self.end),
                                 self.go_to.calculate_euclidean_distance(self.start, self.end))

    def test_goto_obstacle(self):
        valid_path = [(2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
        valid_path2 = [(2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]
        found_path = self.go_to.find_path(level_map_with_obstacle, self.start, self.end)
        found_path2 = self.go_to.find_path(level_map_with_obstacle2, self.start, self.end)
        self.assertListEqual(valid_path, found_path)
        self.assertListEqual(valid_path2, found_path2)

    def test_goto_no_valid_path(self):
        pass


if __name__ == "__main__":
    unittest.main()