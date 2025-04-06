class Mob:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.max_hp = hp
        self.cur_hp = hp
        self.dmg = dmg
        self.alive = True
        
    def take_dmg(self, dmg):
        self.cur_hp -= dmg:
        if self.cur_hp < 0:
            self.alive = False
