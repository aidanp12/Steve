#from magic import magic
from weapon import Weapon

class Player:
    def __init__(self, hp=10):
        # Basic player attributes
        self.max_hp = hp
        self.cur_hp = hp
        #self.mana = mana
        
        # Inventory holds extra items (weapons, armors, spells)
        self.inventory = {
            'weapons': [],
            'items': [],
            #'armors': []
            #'spells': []
        }

        # Starting equipment (can be modified later)
        self.current_weapon = None
        #self.current_armor = None
        #self.current_spell = None

    def equip_weapon(self, weapon):
        """Equip a weapon from the inventory."""
        if weapon.lower() in self.inventory['weapons']:
            self.current_weapon = weapon
            print(f"{weapon} equipped.\n")
        else:
            return f"{weapon} is not in the inventory."

    #def equip_armor(self, armor):
        #"""Equip armor from the inventory."""
        #if armor.lower() in self.inventory['armors']:
            #self.current_armor = armor
            #print(f"{armor} equipped.\n")
        #else:
           #return f"{armor} is not in the inventory."

    #def equip_spell(self, spell):
        #"""Learn a spell from the inventory."""
        #if spell in self.inventory['spells']:
            #self.current_spell = spell
            #print(f"{spell} equipped.\n")
        #else:
            #return f"{spell} is not in the inventory."

    def add_to_inventory(self, item_type, item):
        """Add items to the inventory (weapons, armors)."""
        if item_type not in self.inventory:
            return "Invalid item type. Choose from 'weapons', or 'items'."
        self.inventory[item_type].append(item.lower())

     def remove_from_inventory(self, item_type, item):
         """Remove items from the inventory (weapons and armors)"""
        if item_type not in self.inventory:
            return f"Invalid item type: {item_type}"
        
        try:
            self.inventory[item_type].remove(item)
            print(f"{item.name} has been removed from your inventory.")

            if item_type == 'weapons' and self.current_weapon == item:
                self.current_weapon = None
                print(f"{item.name} has also been unequipped.")
            
           #elif item_type == 'armors' and self.current_armor == item:
                #self.current_armor = None
                #print(f"{item.name} has also been unquipped.")
                
        except ValueError:
            print(f"{item.name} is not in your inventory.")
            
    def view_inventory(self):
        print("Items:")
        if self.inventory['items']:
            for items in self.inventory['items']:
                print(f"- {items}")
        else:
            print("No items in inventory.")
            
        print("Weapons:")
        if self.inventory['weapons']:
            for weapon in self.inventory['weapons']:
                print(f"- {weapon}")
        else:
            print("No weapons in inventory.")

        #rint("Armors:")
        #if self.inventory['armors']:
            #for armor in self.inventory['armors']:
                #print(f"- {armor}")
        #else:
            #print("No armors in inventory.")
        
        #print("Spells:")
        #if self.inventory['spells']:
            #for spell in self.inventory['spells']:
                #print(f"- {spell}")
        #else:
            #print("No spells in inventory.")

    def take_dmg(self, dmg):
        self.cur_hp -= dmg:
