import random


class weapon():
    def __init__(self, name, durability, damage, range, attackSpeed, type, attributes):
        self.name = name
        self.durability = durability
        self.damage = damage
        self.range = int(range)
        self.attackSpeed = attackSpeed #per second
        self.type = type
        self.attributes = attributes
    def printInfo(self):
        print(f"\"{self.name}\": [{self.durability} , {self.damage} ,{self.range} , {self.attackSpeed} , \"{self.type}\", {self.attributes}]") #prints info in an easy dictionay form
 
class mob():
    prevHits = 0
    def __init__(self, name, theme, type, tier, health):
        self.name = name
        self.theme = theme
        self.type = type
        self.tier = tier #used for loot drops , chance and rarity
        self.health = health * tier #not how the scaling will work just concept
        self.weapon = weapon(weapons[int(abs((len(weapons) - 1) * (tier / 4)))]) #inherits the weapon, need to make the seed random but still skewed by the tier
    def attack(player):
        #crits are 1.1 to 1.5 times damage
        crit = 1
        prevHits += 1
        if (random.randint(0,100) < (15 + prevHits * 5)):#20% chance on first hit 
            crit = random.range(1.1,1.5)
            prevHits = 0 #reset counter if crit
        player.health -= mob.weapon.damage * crit #idk how this works in python
'''
MOB TIERS
1: Grunt
2: Elite
3: Commander
4: Mythic
5: Boss

'''
