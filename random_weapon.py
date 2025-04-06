import random

class weaponStats:
  def __init__(self, name, level):
    self.name = name
    self.dmg = 0
    self.rarity = "owo"
    self.dur = 0
    self.pierce = 0
    self.level = level
    self.createStats()
  
  def createStats(self):
    #stat_list = []
    #list1 = [1, 2]
    #sides = [4, 6, 8, 10, 12, 20]
    #tempNum = 0
    #values = [1, 2, 3]
    #for num in range(len(values.length()):
      #tempRand = random.randint(30, 100)
      #temp1 = random.randint(list1[random.randint[1, 2]], tempRand)
      #temp2 = random.randint(sides[random.randint[1, 6]], tempRand)
      #if num == 1:
        #dmg = (temp2 - temp1)*self.level
      #elif num == 2:
        #dur = (temp2 - temp1)*self.level
      #elif num == 3:
        #pierce = (temp2 - (2*temp1))*self.level
    #self.dmg = dmg
    #self.dur = dur
    #self.pierce = pierce
    sides = [4, 6, 8, 10, 12, 20]

    tempRand = random.randint(30, 100)
    temp1 = random.randint(1, tempRand)
    temp2 = random.randint(random.choice(sides), tempRand)

    self.dmg = max((temp2 - temp1) * self.level, 1)
    self.dur = max((temp2 - temp1) * self.level + 5, 1)
    self.pierce = max((temp2 - (2 * temp1)) * self.level, 0)

def __str__(self):
    return f"{self.name.title()} (DMG: {self.dmg}, DUR: {self.dur}, PRC: {self.pierce})"

def __repr__(self):
    return self.__str__()
