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
        self.my_position = (2, 3)
        self.keep_distance_from = (2, 4)

    """ self.keep_distance.find_path() will return a path that should end with a point that's
        exactly 4 steps away from the target. 
        Also, the path should not be longer than 4 steps; That's because in practice, we want to be able
        to e.g. shoot at the target. If we run around the obstacle we might keep the distance but we will 
        lose the target from sight. """
    def test_keep_distance_no_obstacles(self):
        final_position = self.keep_distance.find_path(level_map, self.my_position, self.keep_distance_from)
        self.assertEqual(self.keep_distance.calculate_manhattan_distance(final_position[-1], self.keep_distance_from),
                         4)
        self.assertEqual(len(final_position), 4)

    def test_keep_distance_obstacle(self):
        pass

    def test_keep_distance_no_valid_distance(self):
        pass


if __name__ == "__main__":
    unittest.main()
