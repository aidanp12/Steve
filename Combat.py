from Player import Player
from Mob import Mob
import random

class Combat:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.valid_inputs = ["1", "2", "3", "attack", "items", "run"]
        self.menu()
        self.victory = None
    
    def menu(self):
        counter = 1
        for enemy in self.enemies:
            if enemy.alive:
                print(f"{counter}) {enemy.name}: {enemy.cur_hp}/{enemy.max_hp}\n")
                counter += 1

        print(f"Player HP: {self.player.cur_hp}/{self.player.max_hp}    Player MP: {self.player.mana}\n\n")
        
        while True:
            u_input = input("Options:\n1) Attack\n2) Items\n3) Run\n")
            if u_input in self.valid_inputs:
                self.encounter(u_input)
                break

    def encounter(self, u_input):
        if u_input == "1" or u_input.lower() == "attack":
            if not self.player.current_weapon:
                print("You have no weapon equipped!")
                return
            
            print(f"Equipped Weapon: {self.player.current_weapon.name if self.player.current_weapon else 'None'}")
            self.attack()

            if self.victory():
                print("Combat ended.")
            else:
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
    
    def attack(self):
        '''Accesses player class for weapon and magic, accessing the respective classes for both'''
        living_enemies = [e for e in self.enemies if e.alive]
        
        print("Choose an enemy to attack:\n")
        for idx, enemy in enumerate(living_enemies, start=1):
            print(f"{idx}) {enemy.name}: {enemy.cur_hp}/{enemy.max_hp}")

        while True:
            try:
                choice = int(input("\nEnter enemy number: "))-1
                if 0 <= choice < len(living_enemies):
                    target = living_enemies[choice]
                    dmg = self.player.current_weapon.dmg + self.player.current_weapon.pierce
                    print(f"\nYou attack {target.name} with {self.player.current_weapon} for {dmg} damage!\n")
                    target.take_dmg(dmg)
                    self.player.current_weapon.dur -= 1

                    if self.player_weapon.dur == 0:
                        print(f"{self.player.current_weapon.name} has broken!")
                        
                    if not any(enemy.alive for enemy in self.enemies):
                        self.victory = True
                        print("All enemies defeated!")
                    return

                else:
                    print("Invalid selection. Try again.")

            except ValueError:
                print("Please enter a valid input")

    def items(self):
        #Access the player's inventory
        while True:
            u_input = input("1) Weapon\n2) Armor\n3) Equip\n4) Back")

            if u_input == "1" or u_input.lower() == "weapon":
                print(f"{self.player.inventory['weapons']}\n")

            elif u_input == "2" or u_input.lower() == "armor":
                print(f"{self.player.inventory['armors']}\n")

            #elif u_input == "3" or u_input.lower() == "magic":
                #print(f"{self.player.inventory['spells']}\n")

            elif u_input == "3" or u_input.lower() == "equip":
                e_input = input('Equip: ')
                self.player.equip_weapon(e_input)
        
            elif u_input == "4" or u_input.lower() == 'back':
                break

    def run(self):
        run_chance = .5 #50% chance
        return random.random() < run_chance
