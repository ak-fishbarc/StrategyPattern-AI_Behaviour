import unittest
from HasBehaviour import IsAggressive, IsDefensive, IsCowardly
from ItemsCore import Item
from SpellsCore import Spell
from Inventory import Inventory, Equipment
from Spellbook import Spellbook


class TestHasBehaviourAttack(unittest.TestCase):

    def setUp(self):
        self.test_aggressive = IsAggressive()
        self.test_defensive = IsDefensive()
        self.test_cowardly = IsCowardly()

        self.test_sword = Item("Sword", "weapon", 3, 0, 1)
        self.test_greatsword = Item("Greatsword", "weapon", 6, 0, 1)

        self.test_inventory = Inventory("TagImaginaryEntity", 10)
        self.test_inventory.add_item(self.test_sword)
        self.test_inventory.add_item(self.test_greatsword)
        self.items_list = self.test_inventory.show_items()

        self.test_equipment = Equipment("TagImaginaryEntity", "Greatsword", None, None)

        self.test_spell = Spell(1, 3, 3, 1)

        self.test_spellbook = Spellbook("TagImaginaryEntity", 1)
        self.test_spellbook.add_spell(self.test_spell)
        self.spell_list = self.test_spellbook.show_spell(11)

    """ Test if the owner of IsAggressive is choosing the most damaging weapon 
        or spell. """
    def test_aggressive_close_quarters(self):
        best_damage_item = self.test_aggressive.attack(self.items_list, self.test_equipment,
                                                       self.spell_list, (2, 3), (2, 4))
        self.assertEqual(self.test_greatsword.show_name(), best_damage_item.show_name())
        self.assertEqual(self.test_greatsword.show_damage(), best_damage_item.show_damage())

    def test_aggressive_long_distance(self):
        pass

    def test_aggressive_spell(self):
        pass

