""" Prototype for testing. """


class Inventory:
    def __init__(self, owner, space):
        self.owner = owner
        self.space = space
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.space:
            self.items.append(item)
        else:
            print("Not enough space!")

    def show_items(self):
        return self.items


class Equipment:
    def __init__(self, owner, weapon, shield, armor):
        self.owner = owner
        self.weapon = weapon
        self.shield = shield
        self.armor = armor

    def equip_weapon(self, item, inventory):
        if item.item_type == "weapon":
            if self.weapon is None:
                self.weapon = item
            else:
                inventory.add_item(self.weapon)
                self.weapon = item

        else:
            print("I can't equip that!")

    def show_weapon(self):
        return self.weapon