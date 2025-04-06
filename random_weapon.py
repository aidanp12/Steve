import random

class weaponStats:
  def __init__(self, name, level):
    self.name = name
    self.dmg = 0
    self.rarity = "owo"
    self.dur = 0
    self.pierce = 0
    self.level = level
  
  def createStats():
    stat_list = []
    list1 = [1, 2]
    sides = [4, 6, 8, 10, 12, 20]
    tempNum = 0
    values = [1, 2, 3]
    for num in range(values.length()):
      tempRand = random.randint(30, 100)
      temp1 = random.randint(list1[random.randint[1, 2]], tempRand)
      temp2 = random.randint(sides[random.randint[1, 6]], tempRand)
      if num == 1:
        dmg = (temp2 - temp1)*self.level
      elif num == 2:
        dur = (temp2 - temp1)*self.level
      elif num == 3:
        pierce = (temp2 - (2*temp1))*self.level
    self.dmg = dmg
    self.dur = dur
    self.pierce = pierce
