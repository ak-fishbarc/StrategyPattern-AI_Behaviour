import unittest
from HasBehaviour import IsAggressive


def calculate_manhattan_distance(position1, position2):
    result = abs(position1[1] - position1[0]) + abs(position2[1] - position2[0])
    return result


class TestHasBehaviour(unittest.TestCase):

    """ Test if the owner of IsAggressive is moving towards the target:
    This test assumes that the owner of the function is able to move in a straight line
    without any obstacles on the way. """
    def test_aggressive(self):
        self.testAggressive = IsAggressive()
        move_result = self.testAggressive.move((3,3), (5,5))
        test_move_result = calculate_manhattan_distance((3,3), move_result)
        test_against_value = calculate_manhattan_distance((3,3), (5,5))
        self.assertLess(test_against_value, test_move_result)


if __name__ == "__main__":
    unittest.main()
