import unittest
from Pathfinders import KeepDistance

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]


class TestPathfindersKeepDistance(unittest.TestCase):

    def setUp(self):
        self.keep_distance = KeepDistance()
        self.start = (2, 3)
        self.end = (2, 4)

    def test_keep_distance_no_obstacles(self):
        pass

    def test_keep_distance_obstacle(self):
        pass

    def test_keep_distance_no_valid_distance(self):
        pass


if __name__ == "__main__":
    unittest.main()
