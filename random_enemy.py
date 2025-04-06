from roll import rollDice
class enemyStats:
  def createStats:
    stat_list = []
    type_list = ["Dragon", "Griffin", "Phoenix", "Troll", "Goblin", "Orc", "Vampire", "Werewolf", "Zombie", "Wraith", "Basilisk", "Hydra", "Lich", "Minotaur", "Golem", "Centaur", "Elf", "Dwarf", "Fairy", "Chimera", "Kraken", "Beholder", "Medusa", "Manticore", "Succubus", "Incubus", "Dark Knight", "Shade", "Ghoul", "Wyvern", "Giant Spider", "Giant", "Kobold", "Yeti", "Salamander", "Sphinx", "Unicorn", "Nymph", "Satyr", "Banshee", "Twi'lek", "Djinn", "Elemental", "Frost Giant", "Wyrm", "Gargoyle", "Bugbear", "Direwolf", "Sandworm", "Shadow Beast", "Nightmare", "Twi'ri", "Lamia", "Djinn", "Faun"]
    name = type_list[1d50]
    max_hp = rollDice(1d50)
    dmg = rollDice(5d4)
    ambush = rollDice(1d2)
    
    stat_list.append(name)
    stat_list.append(hp)
    stat_list.append(dmg)
    stat_list.append(ambush)
  return stat_list
