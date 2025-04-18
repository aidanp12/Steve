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

    def equip_weapon(self, weapon_name):
        """Equip a weapon from the inventory."""
        #if weapon_name.lower() in self.inventory['weapons']:
            #self.current_weapon = weapon_name
            #print(f"{weapon_name} equipped.\n")
        #else:
            #print(f"{weapon_name} is not in the inventory.")
        weapon_name = weapon_name.lower()
        for weapon in self.inventory['weapons']:
            if weapon.name.lower() == weapon_name:
                self.current_weapon = weapon
                print(f"{weapon.name} equipped.\n")
                return
            print(f"{weapon_name} is not in the inventory.")

    def unequip_weapon(self):
        if self.current_weapon != None:
            self.current_weapon = None
            print("Weapon unequipped.")
        else:
            print("No weapon to unequip.")


    def add_to_inventory(self, item_type, item_name, item_level=0):
        if (item_type == 'items'):
            self.inventory['items'].append(item_name.lower())
        else:
            new_weapon = weaponStats(item_name.lower(), item_level)
            self.inventory['weapons'].append(new_weapon)

    def remove_from_inventory(self, item_type, item_name):
         #item_name = item_name.lower()
         #for item in self.inventory[item_type]:
            #if item_name == item_name.lower():
                 #self.inventory[item_type].remove(item)
                 #print(f"{item_name} has been removed from your inventory.")
            #if item_type == 'weapons' and self.current_weapon == item.name.lower():
                #self.current_weapon = None
                #print(f"{item_name.name} has also been unequipped.")
            #else:
                #print(f"{item_name} not found in inventory.")
        if not isinstance(item_name, str) and hasattr(item_name, 'name'):
            item_name = item_name.name
        
        item_name = item_name.lower()
        for item in self.inventory[item_type]:
            if item_type == 'weapons' and hasattr(item, 'name') and item.name.lower() == item_name:
                self.inventory[item_type].remove(item)
                print(f"{item.name} has been removed from your inventory.")
                if self.current_weapon and self.current_weapon.name.lower() == item_name:
                    self.current_weapon = None
                    print(f"{item.name} has also been unequipped.")
                return

            elif item_type == 'items' and isinstance(item, str) and item.lower() == item_name:
                self.inventory[item_type].remove(item)
                print(f"{item} has been removed from your inventory.")
                return

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
        self.cur_hp -= dmg
