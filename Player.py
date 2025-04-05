class Player:
    def __init__(self, name, hp, mana):
        # Basic player attributes
        self.name = name
        self.hp = hp
        self.mana = mana

        # Inventory holds extra items (weapons, armors, spells)
        self.inventory = {
            'weapons': [],
            'armors': [],
            'spells': []
        }

        # Starting equipment (can be modified later)
        self.current_weapon = None
        self.current_armor = None
        self.current_spell = None

    def equip_weapon(self, weapon):
        """Equip a weapon from the inventory."""
        if weapon in self.inventory['weapons']:
            self.current_weapon = weapon
            print(f"{self.name} equipped {weapon}.")
        else:
            print(f"{weapon} is not in the inventory.")

    def equip_armor(self, armor):
        """Equip armor from the inventory."""
        if armor in self.inventory['armors']:
            self.current_armor = armor
            print(f"{self.name} equipped {armor}.")
        else:
            print(f"{armor} is not in the inventory.")

    def equip_spell(self, spell):
        """Learn a spell from the inventory."""
        if spell in self.inventory['spells']:
            self.current_spell = spell
            print(f"{self.name} learned {spell}.")
        else:
            print(f"{spell} is not in the inventory.")

    def add_to_inventory(self, item_type, item):
        """Add items to the inventory (weapons, armors, spells)."""
        if item_type not in self.inventory:
            print("Invalid item type. Choose from 'weapons', 'armors', or 'spells'.")
            return
        
        self.inventory[item_type].append(item)
        print(f"{item} added to {item_type} inventory.")
