import HasBehaviour


class IsEntity:

    def __init__(self, behaviour: HasBehaviour, level_map, my_position, target,
                 inventory, equipment, spellbook):
        self.behaviour = behaviour
        self.level_map = level_map
        self.my_position = my_position
        self.target = target
        self.inventory = inventory
        self.equipment = equipment
        self.spellbook = spellbook

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def move(self, level_map, my_position, target):
        self.my_position = self.behaviour.move(level_map, my_position, target)

    def attack(self, inventory, equipment, spellbook, my_position, target):
        self.behaviour.attack(inventory, equipment, spellbook, my_position, target)


