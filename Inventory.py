""" Prototype for testing. """


class Inventory:
    def __init__(self, owner, space):
        self.owner = owner
        self.space = space
        self.items = []


class Equipment:
    def __init__(self, owner, weapon, shield, armor):
        self.owner = owner
        self.weapon = weapon
        self.shield = shield
        self.armor = armor
