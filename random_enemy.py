import random

class enemyStats:
  def __init__(self, name, level):
    self.name = name
    self.level = level
    self.max_hp = 0
    self.cur_hp = 0
    self.dmg = 0
    self.alive = True
    self.ambush = False
    self.createStats()
    
  def createStats(self):
    list1 = [1, 2]
    sides = [4, 6, 8, 10, 12, 20]
    tempNum = 0
    values = [1, 2]
    for num in range(values.length()):
      tempRand = random.randint(30, 100)
      temp1 = random.randint(list1[random.randint[1, 2]], tempRand)
      temp2 = random.randint(sides[random.randint[1, 6]], tempRand)
      if num == 1:
        max_hp = (temp2 - temp1)*self.level
      elif num == 2:
        dmg = (temp2 - temp1)*self.level
    self.max_hp = max_hp
    self.cur_hp = max_hp
    self.dmg = dmg
    temp = random.randint(1,2)
    if temp == 1:
      ambush = True
    else:
      ambush = False
