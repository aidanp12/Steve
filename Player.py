#from magic import magic
from weapon import Weapon
from random_weapon import weaponStats

class Player:
    def __init__(self, hp=10):
        self.max_hp = hp
        self.cur_hp = hp
        self.current_weapon = None
        self.inventory = {
            'weapons': [],
            'items': [],
        }

    def equip_weapon(self, weapon):
        """Equip a weapon from the inventory."""
        if weapon.lower() in self.inventory['weapons']:
            self.current_weapon = weapon
            print(f"{weapon} equipped.\n")
        else:
            print(f"{weapon} is not in the inventory.")

    def unequip_weapon(self):
        """unequip a weapon from the inventory."""
        if self.current_weapon != None:
            self.current_weapon = None
            print("Weapon unequipped.")
        else:
            print("No weapon to unequip.")


    def add_to_inventory(self, item_type, item_name):
        if (item_type == 'items'):
            self.inventory['items'].append(item_name.lower())
        else:
            new_weapon = Weapon(item_name.lower(), weaponStats[0], weaponStats[1], weaponStats[2], weaponStats[3], weaponStats[4], weaponStats[5])
            self.inventory['weapons'].append(new_weapon)

     def remove_from_inventory(self, item_type, item_name):
         item_name = item_name.lower()
         for item in self.inventory[item_type]:
             if item_name = item.name.lower():
                 self.inventory[item_type].remove(item)
                 print(f"{item_name} has been removed from your inventory.")
            if item_type == 'weapons' and self.current_weapon == item.name.lower():
                self.current_weapon = None
                print(f"{item_name.name} has also been unequipped.")
        else:
            print(f"{item_name} not found in inventory.")

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

    def take_dmg(self, dmg):
        self.cur_hp -= dmg:
