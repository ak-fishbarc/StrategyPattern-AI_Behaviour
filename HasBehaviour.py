from abc import ABC, abstractmethod
import Pathfinders


class HasBehaviour(ABC):

    # my_position and target take coordinates x and y as tuple.
    @abstractmethod
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass

    @abstractmethod
    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        pass


# Move towards the target.
class IsAggressive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pathfinder = Pathfinders.GoTo().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        weapon_pointer = equipment.show_weapon()
        if weapon_pointer is not None:
            damage_pointer = weapon_pointer.show_damage()
        else:
            damage_pointer = 0

        for item in inventory.show_items():
            if item.show_type() == "weapon" and item.show_damage() > damage_pointer:
                damage_pointer = item.show_damage()
                weapon_pointer = item

        if weapon_pointer is not None:
            equipment.equip_weapon(weapon_pointer, inventory)
        return equipment.show_weapon()


# Keep the distance from the target.
class IsDefensive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pathfinder = Pathfinders.KeepDistance().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        pass


# Run away from the target.
class IsCowardly(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pathfinder = Pathfinders.GoAway().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        pass

