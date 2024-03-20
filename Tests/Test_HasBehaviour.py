import unittest
from HasBehaviour import IsAggressive

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

level_map_with_obstacle = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]


class TestHasBehaviour(unittest.TestCase):

    def setUp(self):
        self.test_aggressive = IsAggressive()

    """ Test if the owner of IsAggressive is moving towards the target:
    This test is checking if function move returns a tuple different from
    the start position for open path and if it returns current position if
    there's no valid path.
    Tests for pathfinding are done separately. """

    def test_aggressive_no_obstacle(self):
        move_result = self.test_aggressive.move(level_map, (3,3), (5,5))
        self.assertIsNotNone(move_result)
        self.assertNotEqual(move_result, (3, 3))

    def test_aggresive_with_obstacle(self):
        move_result = self.test_aggressive.move(level_map_with_obstacle, (3,3), (5,5))
        self.assertIsNotNone(move_result)
        self.assertEqual(move_result, (3, 3))


if __name__ == "__main__":
    unittest.main()
