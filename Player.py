from magic import magic
from weapon import Weapon

class Player:
    def __init__(self, hp, mana):
        # Basic player attributes
        self.max_hp = hp
        self.cur_hp = hp
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
        if weapon.lower() in self.inventory['weapons']:
            self.current_weapon = weapon
            print(f"{weapon} equipped.\n")
        else:
            return f"{weapon} is not in the inventory."

    def equip_armor(self, armor):
        """Equip armor from the inventory."""
        if armor.lower() in self.inventory['armors']:
            self.current_armor = armor
            print(f"{armor} equipped.\n")
        else:
           return f"{armor} is not in the inventory."

    def equip_spell(self, spell):
        """Learn a spell from the inventory."""
        if spell in self.inventory['spells']:
            self.current_spell = spell
            print(f"{spell} equipped.\n")
        else:
            return f"{spell} is not in the inventory."

    def add_to_inventory(self, item_type, item):
        """Add items to the inventory (weapons, armors, spells)."""
        if item_type not in self.inventory:
            return "Invalid item type. Choose from 'weapons', 'armors', or 'spells'."
        self.inventory[item_type].append(item.lower())
    
    def view_inventory(self):
        print("Weapons:")
        if self.inventory['weapons']:
            for weapon in self.inventory['weapons']:
                print(f"- {weapon}")
        else:
            print("No weapons in inventory.")

        print("Armors:")
        if self.inventory['armors']:
            for armor in self.inventory['armors']:
                print(f"- {armor}")
        else:
            print("No armors in inventory.")
        
        print("Spells:")
        if self.inventory['spells']:
            for spell in self.inventory['spells']:
                print(f"- {spell}")
        else:
            print("No spells in inventory.")
