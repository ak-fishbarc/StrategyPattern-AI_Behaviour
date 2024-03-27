from abc import ABC, abstractmethod
import Pathfinders


class MovementPatterns:
    def move_towards(self, level_map, my_position, target):
        pathfinder = Pathfinders.GoTo().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position

    def keep_distance(self, level_map, my_position, target):
        pathfinder = Pathfinders.KeepDistance().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position


class WeaponChoice:
    def best_damage(self, inventory, equipment):
        weapon_pointer = equipment.show_weapon()
        if weapon_pointer is not None:
            damage_pointer = weapon_pointer.show_damage()
        else:
            damage_pointer = 0

        for item in inventory.show_items():
            if item.show_type() == "weapon" and item.show_range() == 1 and item.show_damage() > damage_pointer:
                damage_pointer = item.show_damage()
                weapon_pointer = item

        if weapon_pointer is not None:
            equipment.equip_weapon(weapon_pointer, inventory)

    def best_defensive(self, inventory, equipment):
        weapon_pointer = equipment.show_weapon()
        shield_pointer = equipment.show_shield()
        if weapon_pointer is not None:
            damage_pointer = weapon_pointer.show_damage()
        else:
            damage_pointer = 0

        if shield_pointer is not None:
            defense_pointer = shield_pointer.show_defense()
        else:
            defense_pointer = 0

        for item in inventory.show_items():
            if item.show_type() == "shield" and item.show_defense() > defense_pointer:
                defense_pointer = item.show_defense()
                shield_pointer = item

        for item in inventory.show_items():
            slots = item.show_slots()
            if shield_pointer is not None:
                if item.show_type() == "weapon" and item.show_range() == 1 and item.show_damage() > damage_pointer \
                        and slots == 1:
                    damage_pointer = item.show_damage()
                    weapon_pointer = item
            else:
                if item.show_type() == "weapon" and item.show_range() == 1 and item.show_damage() > damage_pointer \
                        and slots == 2:
                    damage_pointer = item.show_damage()
                    weapon_pointer = item

        if weapon_pointer is not None:
            equipment.equip_weapon(weapon_pointer, inventory)
        if shield_pointer is not None:
            equipment.equip_shield(shield_pointer, inventory)

    def best_ranged(self, inventory, equipment):
        weapon_pointer = equipment.show_weapon()
        if weapon_pointer is not None:
            damage_pointer = weapon_pointer.show_damage()
        else:
            damage_pointer = 0
        for item in inventory.show_items():
            if item.show_type() == "weapon" and item.show_range() > 1 and item.show_damage() > damage_pointer:
                damage_pointer = item.show_damage()
                weapon_pointer = item
        if weapon_pointer is not None:
            equipment.equip_weapon(weapon_pointer, inventory)


class HasBehaviour(ABC):

    # my_position and target take coordinates x and y as tuple.
    @abstractmethod
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass

    @abstractmethod
    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        pass


""" Move towards the target and chose the most damaging weapon/spell. 
    Pick only melee weapons as using ranged weapons would prevent you from getting closer 
    to the target. In more developed program, this could depend on the entity's class.
    Ranged classes would choose ranged weapons or different behaviour e.g. IsRangedAggressive. 
    Same for spell-casters."""


class IsAggressive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        movement_pattern = MovementPatterns()
        return movement_pattern.move_towards(level_map, my_position, target)

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        weapon_choice = WeaponChoice()
        weapon_choice.best_damage(inventory, equipment)


""" Keep distance from the target. Use ranged weapon or spells when possible or best defensive equipment. """


class IsDefensive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        movement_pattern = MovementPatterns()
        return movement_pattern.keep_distance(level_map, my_position, target)

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        weapon_choice = WeaponChoice()
        distance_calculator = Pathfinders.DistanceCalculator()
        if distance_calculator.calculate_manhattan_distance(my_position, target) == 1:
            weapon_choice.best_defensive(inventory, equipment)
        if distance_calculator.calculate_manhattan_distance(my_position, target) > 1:
            weapon_choice.best_ranged(inventory, equipment)


""" Run away from the target. Do not take any attack actions."""


class IsCowardly(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pathfinder = Pathfinders.GoAway().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position

    def attack(self, inventory, equipment, spellbook: dict, my_position: tuple, target: tuple):
        pass

