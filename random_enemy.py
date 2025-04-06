from roll import rollDice
class enemyStats:
  def createStats:
    stat_list = []
    max_hp = rollDice(1d50)
    dmg = rollDice(5d4)
    ambush = rollDice(1d2)

    stat_list.append(hp)
    stat_list.append(dmg)
    stat_list.append(ambush)
  return stat_list
