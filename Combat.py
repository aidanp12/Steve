from Player import Player
from Mob import Mob

class Combat:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob
        self.valid_inputs = ["1", "2", "3", "attack", "items", "run"]
        self.menu()
    
    def menu(self):
        print(f"{self.mob}: {self.mob.hp}\n")
        print(f"Player HP: {self.player.hp}    Player MP: {self.player.mana}\n\n")
        
        while True:
            u_input = input("Options:\n1) Attack\n2) Items\n3) Run\n")
            if u_input in self.valid_inputs:
                self.encounter(u_input)
                break;

    def encounter(self, u_input):
        if u_input == "1" or u_input.lower() == "attack":
            a_input = input(f"1) {self.player.magic}    2) {self.weapon}")
            self.attack(a_input)
            self.menu()

        elif u_input == "2" or u_input.lower() == "items":
            self.items()
            self.menu()

        elif u_input == "3" or u_input.lower() == "run":
            if self.run():
                print("Sucessfully ran!")
            else:
                print("Couldn't escape!")
                self.menu()
    
    def attack(self, input):
        '''Accesses player class for weapon and magic, accessing the respective classes for both'''
        print('Attack dealt\n')

    def items(self):
        #Access the player's inventory
        while True:
            u_input = input("1) Weapon\n2) Armor\n3) Magic\n 4) Back\n5) Equip\n")

            if u_input == "1" or u_input.lower() == "weapon":
                print(f"{self.player.inventory['weapons']}\n")

            elif u_input == "2" or u_input.lower() == "armor":
                print(f"{self.player.inventory['armors']}\n")

            elif u_input == "3" or u_input.lower() == "magic":
                print(f"{self.player.inventory['spells']}\n")

            elif u_input == "4" or u_input.lower() == "equip":
                e_input = input('Equip: ')
                self.players.equip_weapon(e_input)
        
            elif u_input == "5" or u_input.lower() == 'back':
                break

    def run(self):
        #some formula to calculate run
        return True
