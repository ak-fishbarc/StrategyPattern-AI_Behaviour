import unittest
from HasBehaviour import IsAggressive, IsDefensive, IsCowardly
from Tests import ToolsForTesting as TFT

level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

level_map_with_obstacle = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 5, 5],
                           [0, 0, 0, 5, 0]]

level_map_large = [[0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0]]


class TestHasBehaviour(unittest.TestCase):

    def setUp(self):
        self.test_aggressive = IsAggressive()
        self.test_defensive = IsDefensive()

    """ Test if the owner of IsAggressive is moving towards the target:
    This test is checking if function move returns a tuple different from
    the start position for open path and if it returns current position if
    there's no valid path.
    Tests for pathfinding are done separately. """

    def test_aggressive_no_obstacle(self):
        move_result = self.test_aggressive.move(level_map, (2,2), (4,4))
        self.assertIsNotNone(move_result)
        self.assertNotEqual(move_result, (3, 3))

    def test_aggresive_with_obstacle(self):
        move_result = self.test_aggressive.move(level_map_with_obstacle, (3,3), (5,5))
        self.assertIsNotNone(move_result)
        self.assertEqual(move_result, (3, 3))

    """ Test if the owner of IsDefensive is moving within the distance of 
        4 steps away from the target """

    def test_defensive_no_obstacle(self):
        my_position = (3, 3)
        my_position2 = (3, 3)
        target = (4, 4)
        target2 = (4, 4)
        counter = 1

        while counter < 5:
            counter += 1

            """ Test on small level_map """
            move_result = self.test_defensive.move(level_map, my_position, target)
            my_position = move_result
            distance_from_target = TFT.calculate_manhattan_distance(my_position, target)
            self.assertGreaterEqual(distance_from_target, 1)
            self.assertLessEqual(distance_from_target, 5)

            """ Test on large map to make sure that points are within range of 1 and 5 """

            move_result = self.test_defensive.move(level_map_large, my_position2, target2)
            my_position2 = move_result
            distance_from_target = TFT.calculate_manhattan_distance(my_position2, target2)
            self.assertGreaterEqual(distance_from_target, 1)
            self.assertLessEqual(distance_from_target, 5)


if __name__ == "__main__":
    unittest.main()
