from Player import Player
from Mob import Mob
import random
from roll import diceRoll
from weapon import Weapon
#from Armor import Armor
'''This line is for testing'''

class Combat:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.valid_inputs = ["1", "2", "3", "attack", "items", "run"]
        self.victory = None
        self.ambushdone = False
        self.menu()
        
    def menu(self):
        if self.victory == False:
            return
        
        if not self.ambushdone and any(mob.ambush for mob in self.enemies):
            print("Ambush! Enemies attack first!")
            self.mob_attack()
            self.ambushdone = True

        counter = 1
        for enemy in self.enemies:
            if enemy.alive:
                print(f"{counter}) {enemy.name}: {enemy.cur_hp}/{enemy.max_hp}")
                counter += 1
        print()
        print(f"Player HP: {self.player.cur_hp}/{self.player.max_hp}")
        
        while True:
            u_input = input("Options:\n1) Attack\n2) Items\n3) Run\n")
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
            else:
                self.mob_attack()
                self.menu()

        elif u_input == "2" or u_input.lower() == "items":
            self.items()
            self.menu()

        elif u_input == "3" or u_input.lower() == "run":
            if self.run():
                print("Sucessfully ran!\n")
            else:
                print("Couldn't escape!\n")
                self.mob_attack()
                self.menu()
    
    def attack(self):
        '''Attacks chosen target provided by input'''
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
                        
                    if not any(enemy.alive for enemy in self.enemies):
                        self.victory = True
                        print("All enemies defeated!")
                    return

                else:
                    print("Invalid selection. Try again.")

            except ValueError:
                print("Please enter a valid input")
    
    def mob_attack(self): 
        '''damage dealt by the mobs one-by-one through the list of them'''
        living_enemies = [e for e in self.enemies if e.alive]
        for enemy in living_enemies:
            dmg = enemy.dmg
            m_dmg = self.attack_modifier(dmg)
            print(f"{enemy.name} attacks you for {m_dmg} damage!")

            #if self.player.current_armor:
                #f_dmg = self.defense_modifier(m_dmg)
            #else:
                #f_dmg = m_dmg

            self.player.take_dmg(m_dmg)
            print(f"You took {m_dmg} damage!\n")

            if self.player.cur_hp <= 0:
                self.victory = False
                print("You Died T_T\n")
                return

    def items(self):
        '''Accesses the player's inventory during combat encounter'''
        while True:
            u_input = input("\n1) Weapon\n2) Armor\n3) Equip\n4) Back\n")

            if u_input == "1" or u_input.lower() == "weapon":
                print(f"{self.player.inventory['weapons']}\n")

            #elif u_input == "2" or u_input.lower() == "armor":
                #print(f"{self.player.inventory['armors']}\n")

            elif u_input == "3" or u_input.lower() == "equip":
                e_input = input('Equip: ')
                self.player.equip_weapon(e_input)
        
            elif u_input == "4" or u_input.lower() == 'back':
                break

    def attack_modifier(self, base_dmg):
        '''Damage modifier has a chance of increasing or decreasing damage dealt, as well as keeping normal damage based on 1d20'''
        roll = diceRoll("1d20")
        
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
    
    #def defense_modifier(self, dmg):
        #'''Reduces damage by base defense of armour + bonus reduction depending on 1d20 roll'''
        #roll = diceRoll("1d20")
        #base_defense = self.player.current_armor.defense

        #if 1 < roll < 20:
            #modifier = roll *0.05

        #elif roll == 20:
            #modifier = 2
            #print("Perfect block!")
        #else:
            #modifier = 0

        #bonus_defense = base_defense * modifier
        #reduced_dmg = round(dmg - bonus_defense - base_defense, 2)
        #reduced_dmg = max(0, reduced_dmg)

        #absorbed = dmg - reduced_dmg
        #durability_loss = max(1, int(absorbed/5))
        #self.player.current_armor.dur -= durability_loss

        #if self.player.current_armor.dur == 0:
                #print(f"{self.player.current_armor.name} has broken!")
                #self.player.remove_from_inventory('armors', self.player.current_armor)
                #self.player.current_armor = None
        #print(f"Damage was reduced by {absorbed} becuase of your armor!")
        #return(reduced_dmg)
    
    def run(self):
        run_chance = .5 #50% chance
        return random.random() < run_chance
    
def main():
    # Create a player with 20 HP
    player = Player(hp=20)

    # Create a weapon and armor
    sword = Weapon(dmg_type="slashing", dmg=5, rarity="common", dur=5, pierce=1)
    sword.name = "Iron Sword"  # Add name for display
    #armor = Armor(name="Leather Armor", dur=10, defense=2, rarity="common")

    # Add items to inventory and equip them
    player.add_to_inventory('weapons', sword.name.lower())
    player.current_weapon = sword

    #player.add_to_inventory('armors', armor.name.lower())
    #player.current_armor = armor

    # Create some mobs
    goblin = Mob(name="Goblin", hp=10, dmg=3, ambush=True)
    skeleton = Mob(name="Skeleton", hp=12, dmg=4, ambush=False)

    # Start combat
    combat = Combat(player, [goblin, skeleton])

main()
    combat = Combat(player, [goblin, skeleton])

main()
