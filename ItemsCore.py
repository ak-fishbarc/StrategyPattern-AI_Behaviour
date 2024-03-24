""" Prototype for testing.
    This class could be split in to a few to cover items like weapons, shields, armors, etc.
    There would be more parameters like cost, weight, etc."""


class Item:
    def __init__(self, damage, defense, attack_range):
        self.damage = damage
        self.defense = defense
        self.attack_range = attack_range


