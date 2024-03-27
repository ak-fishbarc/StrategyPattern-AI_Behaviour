import unittest
from HasBehaviour import IsAggressive, IsDefensive
from IsEntity import IsEntity
from Pathfinders import DistanceCalculator
from Inventory_and_Items.Inventory import Inventory, Equipment
from Inventory_and_Items.ItemsCore import Item
from Spellbook_and_Spells.Spellbook import Spellbook
from Spellbook_and_Spells.SpellsCore import Spell


level_map = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]


class TestIsEntity(unittest.TestCase):

    def setUp(self):

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

        self.test_entity = IsEntity(IsAggressive(), level_map, (2, 3), (2, 4),
                                    self.test_inventory, self.test_equipment, self.test_spellbook)

    def test_entity(self):
        self.test_entity.move(level_map, (2, 3), (2, 4))
        self.assertEqual(self.test_entity.my_position, (2, 4))

        self.test_entity.attack(self.test_inventory, self.test_equipment, self.test_spellbook,
                                (2, 3), (2, 4))
        self.assertEqual(self.test_greatsword.show_name(), self.test_entity.equipment.show_weapon().show_name())

    def test_entity_change_behaviour(self):
        calculate_distance = DistanceCalculator()
        self.test_entity.set_behaviour(IsDefensive())
        self.test_entity.move(level_map, (2, 3), (2, 4))
        distance_from_new_position = calculate_distance.calculate_manhattan_distance(self.test_entity.my_position, (2, 4))
        self.assertGreater(distance_from_new_position, 1)

        self.test_entity.attack(self.test_entity.inventory, self.test_entity.equipment, self.test_entity.spellbook,
                                self.test_entity.my_position, self.test_entity.target)
        self.assertEqual(self.test_bow.show_name(), self.test_entity.equipment.show_weapon().show_name())


if __name__ == "__main__":
    unittest.main()
