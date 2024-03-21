import unittest
from Pathfinders import KeepDistance

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

level_map_with_obstacle = [[0, 0, 0, 0, 0],
                           [0, 5, 5, 0, 0],
                           [0, 0, 5, 0, 0],
                           [0, 5, 5, 0, 0],
                           [0, 5, 5, 0, 0]]

level_map_no_valid_path = [[0, 0, 5, 0, 0],
                           [0, 5, 5, 0, 0],
                           [0, 0, 5, 0, 0],
                           [0, 5, 5, 0, 0],
                           [0, 5, 5, 0, 0]]


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

    def test_keep_distance_obstacle(self):
        final_position = self.keep_distance.find_path(level_map_with_obstacle, self.my_position, self.keep_distance_from)
        self.assertListEqual([(2, 3), (1, 3), (0, 3), (0, 2)], final_position)

    def test_keep_distance_no_valid_distance(self):
        final_position = self.keep_distance.find_path(level_map_no_valid_path, self.my_position, self.keep_distance_from)
        self.assertListEqual([], final_position)

    def test_keep_distance_no_obstacles_diagonal_position(self):
        my_position = (3, 3)
        keep_distance_from = (4, 4)
        final_position = self.keep_distance.find_path(level_map, my_position, keep_distance_from)
        for position in final_position:
            distance_from_target = self.keep_distance.calculate_manhattan_distance(my_position, keep_distance_from)
            self.assertGreaterEqual(distance_from_target, 1)
            self.assertLessEqual(distance_from_target, 5)
            my_position = position


if __name__ == "__main__":
    unittest.main()
