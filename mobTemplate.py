import random
class weapon():
  def __init__(self,w):
    self.name = w[0]
    self.durability = w[1]
    self.damage = w[2]
    self.range = w[3]
    self.attributes = w[4]
 
class mob():
    prevHits = 0
    def __init__(self, name, theme, type, tier, health, weapon):
        self.name = name
        self.theme = theme
        self.type = type
        self.tier = tier #used for loot drops , chance and rarity
        self.health = health * tier #not how the scaling will work just concept
        self.weapon = weapon #inherits the weapon
    def attack(player):
        #crits are 1.1 to 1.5 times damage
        crit = 1
        prevHits += 1
        if (random.randint(0,100) < (15 + prevHits * 5)):#20% chance on first hit 
            crit = random.range(1.1,1.5)
            prevHits = 0 #reset counter if crit
        player.health -= mob.weapon.damage * crit #idk how this works in python
