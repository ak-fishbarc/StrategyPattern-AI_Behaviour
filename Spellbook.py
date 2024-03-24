""" Prototype for testing. """


class Spellbook:
    def __init__(self, owner, spellbook_level):
        self.owner = owner
        self.spellbook_level = spellbook_level
        self.spellbook = {1: [], 2: [], 3: []}

    def add_spell(self, spell):
        if spell.spell_level == 1 and spell not in self.spellbook[1]:
            self.spellbook[1].append(spell)

    def show_spell(self, level):
        if level == 1:
            return self.spellbook[1]
        elif level == 2:
            return self.spellbook[2]
        elif level == 3:
            return self.spellbook[3]
        elif level == 11:
            return self.spellbook

