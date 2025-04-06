from Player import Player
from Mob import Mob
import random

class Combat:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.valid_inputs = ["1", "2", "3", "attack", "items", "run"]
        self.victory = None
        self.ambushdone = False
        self.menu()
        
    def menu(self):
        counter = 1
        for enemy in self.enemies:
            if enemy.alive:
                print(f"{counter}) {enemy.name}: {enemy.cur_hp}/{enemy.max_hp}\n")
                counter += 1

        if not self.ambushdone and any(mob.ambush for mob in self.enemies):
            print("Ambush! Enemies attack first!")
            mob_attack()
            self.ambushdone = True

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
                self.menu
                return
        
            print(f"Equipped Weapon: {self.player.current_weapon.name if self.player.current_weapon else 'None'}")
            self.attack()

            if self.victory:
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
                    f_dmg = self.dmg_modifier(dmg)
                    
                    if f_dmg > dmg:
                        print(f"Critical Success! You deal an extra {f_dmg-dmg} damage!\n")
                    elif f_dmg < dmg:
                        print(f"Critical Failure! You deal {dmg-f_dmg} less damage!\n")

                    print(f"\nYou attack {target.name} with {self.player.current_weapon} for {dmg} damage!\n")
                    target.take_dmg(dmg)
                    self.player.current_weapon.dur -= 1

                    if self.player.current_weapon.dur == 0:
                        print(f"{self.player.current_weapon.name} has broken!")
                        self.player.remove_from_inventory('weapons', self.player.current_weapon)
                        self.player.current_weapon = None
                        
                    if not any(enemy.alive for enemy in self.enemies):
                        self.victory = True
                        print("All enemies defeated!")
                    return

                else:
                    print("Invalid selection. Try again.")

            except ValueError:
                print("Please enter a valid input")
    
    def mob_attack(self): 
        '''damage dealt by the mobs 1by1 through the list of them'''
        living_enemies = [e for e in self.enemies if e.alive]
        for enemy in living_enemies:
            dmg = enemy.dmg
            f_dmg = self.dmg_modifier(dmg)
            print(f"{enemy.name} attacks you for {dmg} damage!")

            if self.player.current_armor:
                self.player.current_armor.dur -= 1
            self.player.take_dmg(f_dmg)
            
            if self.player.cur_hp <= 0:
                self.victory = False
                print("You Died T_T")
                return
                
            if self.player.current_armor.dur == 0:
                print(f"{self.player.current_armor.name} has broken!")
                self.player.remove_from_inventory('armors', player.current_armor)
                self.player.current_armor = None

    def items(self):
        #Access the player's inventory
        while True:
            u_input = input("1) Weapon\n2) Armor\n3) Equip\n4) Back\n")

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

    def dmg_modifier(base_dmg):
        roll = random.randint(1,20)

        if 1 <= roll <= 8:
            modifier = 1 - ((9-roll) * 0.03)
        elif 9 <= roll <= 12:
            modifier = 1.0
        elif 13 <= roll <= 20:
            modifier = 1 + ((roll - 12) * 0.03)
        else:
            modifier = 1.0

        modified_dmg = round(base_dmg * modifier, 2)
        return modified_dmg
        
    def run(self):
        run_chance = .5 #50% chance
        return random.random() < run_chance
