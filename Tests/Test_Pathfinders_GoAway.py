import unittest
from Pathfinders import GoAway

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

level_map_obstacle = [[5, 5, 5, 5, 5],
                      [5, 0, 0, 0, 5],
                      [5, 0, 0, 0, 5],
                      [5, 0, 0, 0, 5],
                      [5, 5, 5, 5, 5]]

level_map_obstacle2 = [[0, 0, 0, 0, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 0, 0, 0],
                       [0, 5, 5, 5, 0],
                       [0, 0, 0, 0, 0]]


class TestPathfindersGoAway(unittest.TestCase):

    def setUp(self):
        self.go_away = GoAway()
        self.my_position = (2, 3)
        self.go_away_from = (2, 4)

    def test_go_away_no_obstacles(self):
        escape_path = self.go_away.find_path(level_map, self.my_position, self.go_away_from)
        distance_counter = 0
        for point in escape_path:
            distance_counter += 1
            """ Avoid measuring distance from starting position.
                Make sure that with each step it's further away from the target on an empty map """
            if point != self.my_position:
                measure_distance = self.go_away.calculate_manhattan_distance(point, self.go_away_from)
                self.assertEqual(measure_distance, distance_counter)

    def test_go_away_obstacle(self):
        escape_path = self.go_away.find_path(level_map_obstacle, self.my_position, self.go_away_from)
        escape_path2 = self.go_away.find_path(level_map_obstacle2, self.my_position, self.go_away_from)
        print(escape_path)
        print(escape_path2)

        """ Check if the code works when it can't reach the desired distance; 
            In this case, length/height of the level_map.
            Each point should be further away from the target. """
        distance_counter = 0
        for point in escape_path:
            distance_counter += 1
            if point != self.my_position:
                measure_distance = self.go_away.calculate_manhattan_distance(point, self.go_away_from)
                self.assertEqual(measure_distance, distance_counter)

        """ Check if find_path won't return any path that tries to walk through
            go_away_from; In this case (2, 4) position. """
        for point in escape_path2:
            self.assertNotEqual(point, self.go_away_from)

    def test_go_away_no_valid_path(self):
        pass


if __name__ == "__main__":
    unittest.main()