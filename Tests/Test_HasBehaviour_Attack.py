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

        self.test_sword = Item("Sword", "weapon", 1, 3, 0, 1)
        self.test_greatsword = Item("Greatsword", "weapon", 2, 6, 0, 1)
        self.test_short_bow = Item("Short Bow", "weapon", 2, 3, 0, 5)
        self.test_bow = Item("Bow", "weapon", 2, 7, 0, 6)
        self.test_shield = Item("Shield", "shield", 1, 0, 3, 0)

        self.test_inventory = Inventory("TagImaginaryEntity", 10)
        self.test_inventory.add_item(self.test_sword)
        self.test_inventory.add_item(self.test_greatsword)
        self.test_inventory.add_item(self.test_short_bow)
        self.test_inventory.add_item(self.test_bow)
        self.test_inventory.add_item(self.test_shield)

        self.test_equipment = Equipment("TagImaginaryEntity", None, None, None)

        self.test_spell = Spell(1, 3, 3, 1)

        self.test_spellbook = Spellbook("TagImaginaryEntity", 1)
        self.test_spellbook.add_spell(self.test_spell)
        self.spell_list = self.test_spellbook.show_spell(11)

    """ Test if the owner of IsAggressive is choosing the most damaging weapon 
        or spell. """
    def test_aggressive(self):
        self.test_aggressive.attack(self.test_inventory, self.test_equipment,
                                    self.spell_list, (2, 3), (2, 4))
        best_weapon = self.test_equipment.show_weapon()
        self.assertEqual(self.test_greatsword.show_name(), best_weapon.show_name())
        self.assertEqual(self.test_greatsword.show_damage(), best_weapon.show_damage())

    def test_defensive_close_quarters(self):
        self.test_defensive.attack(self.test_inventory, self.test_equipment,
                                   self.spell_list, (2, 3), (2, 4))
        best_shield = self.test_equipment.show_shield()
        best_weapon = self.test_equipment.show_weapon()
        self.assertEqual(self.test_shield.show_name(), best_shield.show_name())
        self.assertEqual(self.test_shield.show_defense(), best_shield.show_defense())
        self.assertEqual(self.test_sword.show_name(), best_weapon.show_name())
        self.assertEqual(self.test_sword.show_damage(), best_weapon.show_damage())

    def test_defensive_distance(self):
        self.test_defensive.attack(self.test_inventory, self.test_equipment,
                                   self.spell_list, (2, 3), (2, 4))
        best_ranged = self.test_equipment.show_weapon()
        self.assertEqual(self.test_bow.show_name(), best_ranged.show_name())
        self.assertEqual(self.test_bow.show_damage, best_ranged.show_damage())


if __name__ == "__main__":
    unittest.main()