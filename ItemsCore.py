""" Prototype for testing.
    This class could be split in to a few to cover items like weapons, shields, armors, etc.
    There would be more parameters like cost, weight, etc.
    Item type could use numerical system, in this case it's using strings"""


class Item:
    def __init__(self, item_name, item_type, damage, defense, attack_range):
        self.item_name = item_name
        self.item_type = item_type
        self.damage = damage
        self.defense = defense
        self.attack_range = attack_range

    def show_name(self):
        return self.item_name

    def show_type(self):
        return self.item_type

    def show_damage(self):
        return self.damage

    def show_defense(self):
        return self.defense

    def show_range(self):
        return self.attack_range



