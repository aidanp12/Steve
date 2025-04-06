import random
class enemyStats:
  def createStats():
    stat_list = []
    max_hp = random.randint(1,50)

    rolls = [random.randint(1,4) for _ in range(5)]
    total = sum(rolls)
    dmg = total

    ambush = random.randint(1,2)
    
    stat_list.append(max_hp)
    stat_list.append(dmg)
    stat_list.append(ambush)
    return stat_list
