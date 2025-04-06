from Player import Player
from random_enemy import enemyStats
import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.valid_inputs = ["1", "2", "3", "attack", "items", "run"]
        self.victory = None
        self.ambushdone = False
        self.menu()
        
    def menu(self):
        if self.victory == False:
            return
        if not self.ambushdone and self.enemy.ambush:
            print("Ambush! Enemy attack first!")
            self.mob_attack()
            self.ambushdone = True

            if self.victory is False:
                return

        print(f"{self.enemy.name}: {self.enemy.cur_hp}/{self.enemy.max_hp}")
        print()
        print(f"Player HP: {self.player.cur_hp}/{self.player.max_hp}")
        
        while True:
            u_input = input("Options:\n1) Attack\n2) Run\n")
            if u_input in self.valid_inputs:
                self.encounter(u_input)
                break

    def encounter(self, u_input):
        if u_input == "1" or u_input.lower() == "attack":
            if not self.player.current_weapon:
                print("You have no weapon equipped!")
                self.menu()
                return
        
            print(f"Equipped Weapon: {self.player.current_weapon.name}")
            self.attack()

            if self.victory:
                print("Combat ended.")
                return
            self.mob_attack()

            if self.victory is False:
                return
            self.menu()

        #elif u_input == "2" or u_input.lower() == "items":
            #self.items()
            #self.menu()

        elif u_input == "2" or u_input.lower() == "run":
            if self.run():
                print("Sucessfully ran!\n")
            else:
                print("Couldn't escape!\n")
                self.mob_attack()
                self.menu()
    
    def attack(self):
        '''Attacks chosen target provided by input'''
        target = self.enemy
        dmg = self.player.current_weapon.dmg + self.player.current_weapon.pierce
        f_dmg = self.attack_modifier(dmg)
                    
        if f_dmg > dmg:
            print(f"Critical Success! You deal an extra {f_dmg-dmg} damage!\n")
        elif f_dmg < dmg:
            print(f"Critical Failure! You deal {dmg-f_dmg} less damage!\n")

        print(f"You attack {target.name} with {self.player.current_weapon.name} for {f_dmg} damage!\n")
        target.take_dmg(f_dmg)
        self.player.current_weapon.dur -= 1

        if self.player.current_weapon.dur == 0:
            print(f"{self.player.current_weapon.name} has broken!")
            self.player.remove_from_inventory('weapons', self.player.current_weapon)
            self.player.current_weapon = None
                        
        if not target.alive:
            self.victory = True
            print("All enemies defeated!")
            return
    
    def mob_attack(self): 
        '''damage dealt by the mobs one-by-one through the list of them'''
        dmg = self.enemy.dmg
        m_dmg = self.attack_modifier(dmg)
        print(f"{self.enemy.name} attacks you for {m_dmg} damage!")

        self.player.take_dmg(m_dmg)
        print(f"You took {m_dmg} damage!\n")

        if self.player.cur_hp <= 0:
            self.victory = False
            print("You Died T_T\n")
            return

    def items(self):
        '''Accesses the player's inventory during combat encounter'''
        while True:
            u_input = input("\n1) Weapon\n2) Equip\n3) Back\n")

            if u_input == "1" or u_input.lower() == "weapon":
                print(f"{self.player.inventory['weapons']}\n")

            elif u_input == "2" or u_input.lower() == "equip":
                e_input = input('Equip: ')
                self.player.equip_weapon(e_input.lower())
        
            elif u_input == "3" or u_input.lower() == 'back':
                break

    def attack_modifier(self, base_dmg):
        '''Damage modifier has a chance of increasing or decreasing damage dealt, as well as keeping normal damage based on 1d20'''
        roll = random.randint(1,20)
        
        modifier = 0
        if roll == 1:
            modifier = .5
        elif 2 <= roll <= 5:
            modifier = 1 - ((6-roll) * 0.05)
        elif 6 <= roll <= 15:
            modifier = 1.0
        elif 16 <= roll <= 19:
            modifier = 1 + ((roll - 15) * 0.05)
        elif roll == 20:
            modifier = 1.5
        else:
            modifier = 1.0

        modified_dmg = round(base_dmg * modifier, 2)
        return modified_dmg
    
    def run(self):
        run_chance = .5 #50% chance
        return random.random() < run_chance

    def run(self):
        run_chance = .5 #50% chance
        return random.random() < run_chance
