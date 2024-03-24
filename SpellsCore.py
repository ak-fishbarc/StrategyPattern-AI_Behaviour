""" Prototype for testing. 
    This class could be split in to a few to cover different spell schools, effects, etc."""


class Spell:
    def __init__(self, spell_level, attack, attack_range, cast_speed):
        self.spell_level = spell_level
        self.attack = attack
        self.attack_range = attack_range
        self.cast_speed = cast_speed
