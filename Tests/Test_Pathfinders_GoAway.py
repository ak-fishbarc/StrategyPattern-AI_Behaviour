import unittest
from Pathfinders import GoAway

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]


class TestPathfindersGoAway(unittest.TestCase):

    def setUp(self):
        self.go_away = GoAway()
        self.my_position = (2, 3)
        self.go_away_from = (2, 4)

    def test_go_away_no_obstacles(self):
        pass

    def test_go_away_obstacle(self):
        pass

    def test_go_away_no_valid_path(self):
        pass


if __name__ == "__main__":
    unittest.main()