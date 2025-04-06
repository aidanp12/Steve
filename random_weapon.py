from roll import rollDice

class weaponStats:
  def createStats():
    stat_list = []
    type_list = ["fire", "ice", "electricity", "void", "water", "air"]
    rarity_list = ["common", "uncommon", "rare", "legendary", "mythic", "godlike"]
    dmg_type = type_list[rollDice("1d6")]
    rarity = rarity_list[rollDice("1d6")]
    dmg = rollDice("5d4")
    dur = rollDice("2d50")
    pierce = rollDice("1d10")
    stat_list.append(dmg_type)
    stat_list.append(dmg)
    stat_list.append(rarity)
    stat_list.append(dur)
    stat_list.append(pierce)
    return stat_list
