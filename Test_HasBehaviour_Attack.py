import unittest
from HasBehaviour import IsAggressive, IsDefensive, IsCowardly


class TestHasBehaviourAttack(unittest.TestCase):

    def setUp(self):
        self.test_aggressive = IsAggressive()
        self.test_defensive = IsDefensive()
        self.test_cowardly = IsCowardly()

    """ Test if the owner of IsAggressive is choosing the most damaging weapon 
        or spell. """
    def test_aggressive_close_quarters(self):
        pass

    def test_aggressive_long_distance(self):
        pass

    def test_aggressive_spell(self):
        pass

