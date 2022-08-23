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


#might want to scale up the overall attack speed if it feels too boring
dagger1 = weapon("Iron knife" , 400 , 12 , 1, 2 , "dagger" ,[None])
dagger2 = weapon("Bronze knife" , 500 , 16 , 1, 3 , "dagger" ,[None])
dagger3 = weapon("Steel knife" , 600 , 20 , 2, 4 , "dagger" ,[None])

longsword1 = weapon("Iron Longsword" , 500 , 14 , 2, 0.5 , "longsword" ,[None])
longsword2 = weapon("Bronze Longsword" , 600 , 18 , 3, 0.75 , "longsword" ,[None])
longsword3 = weapon("Steel Longsword" , 700 , 22 , 4 , 1, "longsword" , [None])

handaxe1 = weapon("Stone Axe" , 500 , 15 , 2 , 1 , "handaxe" ,[None])
handaxe2 = weapon("Iron Axe" , 700 , 18 , 2 , 1.25 , "handaxe" ,[None])
handaxe3 = weapon("Steel Axe" , 800 , 21 , 2 , 1.5 , "handaxe" ,[None])

battleaxe1 = weapon("Stone BattleaAxe" , 700 , 18 , 2 , 0.33 , "battleaxe" ,[None])
battleaxe2 = weapon("Iron BattleaAxe" , 800 , 21 , 2 , 0.33 , "battleaxe" ,[None])
battleaxe3 = weapon("Steel BattleaAxe" , 950 , 23 , 3 , 0.33 , "battleaxe" ,[None])

gaultlet1 = weapon("Iron Gauntlet" , 400 , 20 , 1 , 0.5 , "gauntlet" ,[None])
gaultlet2 = weapon("Bronze Gauntlet" , 500 , 22 , 1 , 0.75 , "gauntlet" ,[None])
gaultlet3 = weapon("Steel Gauntlet" , 600 , 25 , 1 , 1 , "gauntlet" ,[None])

mace1 = weapon("Iron Mace" , 500 , 10 , 1 , 1.33 , "mace" ,[None])
mace2 = weapon("Bronze Mace" , 650 , 15 , 1 , 1.66 , "mace" ,[None])
mace3 = weapon("Steel Mace" , 800 , 21 , 1 , 2 , "mace" ,[None])

spear1 = weapon("Iron Spear" , 400 , 13 , 3 , 1 , "spear" , [None])
spear2 = weapon("Steel Spear" , 600 , 17 , 4 , 1.33 , "spear" , [None])
spear3 = weapon("Diamond Spear" , 800 , 22 , 5 , 1.66 , "spear" , [None])

weapons = [dagger1,
    dagger2,
    dagger3, 
    longsword1, 
    longsword2 ,
    longsword3 ,
    handaxe1 ,
    handaxe2 ,
    handaxe3 ,
    battleaxe1, 
    battleaxe2 ,
    battleaxe3 ,
    gaultlet1 ,
    gaultlet2 ,
    gaultlet3 ,
    mace1 ,
    mace2 ,
    mace3 ,
    spear1 ,
    spear2 ,
    spear3
]
for w in weapons:
    w.printInfo()


