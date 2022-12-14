import random

weapons = []
class weapon():
    def __init__(self, name, durability, damage, range, attackSpeed, type, attributes = None):
        self.name = name
        self.durability = durability
        self.damage = damage
        self.range = int(range)
        self.attackSpeed = attackSpeed #per second
        self.type = type
        self.attributes = attributes
    def printInfo(self):
        print(f"\"{self.name}\": [{self.durability} , {self.damage} ,{self.range} , {self.attackSpeed} , \"{self.type}\", {self.attributes}]") #prints info in an easy dictionay form

class rangedWeapon():
    def __init__(self, name, durability, damage, range, attackSpeed, type, attributes = [None]):
        self.name = name
        self.durability = durability
        self.damage = damage #per each shot, #? special arrow types maybe
        self.range = range #how far the projectile goes beofre damage falloff
        self.attackSpeed = attackSpeed #shots per second
        self.type = type
        self.attributes = attributes
    def printInfo(self):
        print(f"\"{self.name}\": [{self.durability} , {self.damage} ,{self.range} , {self.attackSpeed} , \"{self.type}\", {self.attributes}]") #prints info in an easy dictionay form



class armor():
    def __init__(self, name, durability, protection, slot, attributes = [None]):#do add more effectieve types (liek pokemon)?
        self.name = name
        self.durability = durability #the peice will delete itself if it gets below 0
        self.protection = protection #total posible damage absorbed by each peice, it is an expoentially decreasing chance for high blockage
        self.slot = slot #head,chest,leg,feet, hands/wrists?
        self.attributes = attributes
    def printInfo(self):
        print(f"\'{self.name}\': [{self.durability} , {self.protection} , {self.slot} , {self.attributes}]")

class mob():
    prevHits = 0
    def __init__(self, name, theme, type, tier, health, armorList, weapon = weapon(weapons[int(abs((len(weapons) - 1) * (tier / 4)))])):
        self.name = name
        self.theme = theme
        self.type = type
        self.tier = tier #used for loot drops , chance and rarity
        self.health = health * tier #not how the scaling will work just concept
        self.armorList = armorList #list of equiped armor, max 4
        self.weapon = weapon #inherits the weapon, need to make the seed random but still skewed by the tier
    def attack(player):
        #crits are 1.1 to 1.5 times damage
        crit = 1
        prevHits += 1
        if (random.randint(0,100) < (15 + prevHits * 5)):#20% chance on first hit 
            crit = random.range(1.1,1.5)
            prevHits = 0 #reset counter if crit
        player.health -= mob.weapon.damage * crit #idk how this works in python

class player():
    def __init__(self , name , health , weapon):
        self.name = name
        self.health = health
        self.playerWeapon = weapon 
    def attack(self):
        attackRadius = (3.14159 * self.playerWeapon.range * self.playerWeapon.range) #do i need to track positon for player and each mob?
        if mob in attackRadius:
            mob.health -= weapon.damage

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

gauntlet1 = weapon("Iron Gauntlet" , 400 , 20 , 1 , 0.5 , "gauntlet" ,[None])
gauntlet2 = weapon("Bronze Gauntlet" , 500 , 22 , 1 , 0.75 , "gauntlet" ,[None])
gauntlet3 = weapon("Steel Gauntlet" , 600 , 25 , 1 , 1 , "gauntlet" ,[None])

mace1 = weapon("Iron Mace" , 500 , 10 , 1 , 1.33 , "mace" ,[None])
mace2 = weapon("Bronze Mace" , 650 , 15 , 1 , 1.66 , "mace" ,[None])
mace3 = weapon("Steel Mace" , 800 , 21 , 1 , 2 , "mace" ,[None])

spear1 = weapon("Iron Spear" , 400 , 13 , 3 , 1 , "spear" , [None])
spear2 = weapon("Steel Spear" , 600 , 17 , 4 , 1.33 , "spear" , [None])
spear3 = weapon("Diamond Spear" , 800 , 22 , 5 , 1.66 , "spear" , [None])

weapons = [
    dagger1,
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
    gauntlet1 ,
    gauntlet2 ,
    gauntlet3 ,
    mace1 ,
    mace2 ,
    mace3 ,
    spear1 ,
    spear2 ,
    spear3
]

bow1 = rangedWeapon('Wooden Bow' , 400 , 12, 10, 1, 'bow')
crossbow1 = rangedWeapon('Iron Crossbow' , 600 , 21, 15, 1.66, 'crossbow')

helmet1 = armor("Iron Helm" , 600, 1, 'head')
chest1 = armor('Iron Chest', 800, 4, 'chest')
legging1 = armor('Iron Leggings', 700, 2, 'legging')
boot1 = armor('Iron Boots', 500, 1, 'boot')

armors = [
    helmet1,
    chest1,
    legging1,
    boot1
]

#* ARES KIT
AresSword = weapon("Sword of Mars" , 1000 , 30 , 2 , 1 , "sword" , [None])
AresHelm = armor("Ares Helm", 100, 10, 'head')
AresChest = armor("Ares Chest", 100, 15, 'chest')
AresLeggings = armor("Ares Leggings" , 100, 10, 'legging')
AresBoots = armor("Ares Boots", 100, 5, 'boot')

Ares = mob("Ares" , "greek" , "greek" , 5 , 250 , [AresHelm,AresChest,AresLeggings,AresBoots] ,AresSword)


#*Hades Kit
hadesBattleaxe = weapon("Fiery Axe of Hellblaze" , 1000, 40, 3,  0.5, "battleaxe", [None])
hadesHelm = armor("Hades Helm", 100, 10, 'head')
hadesChest = armor("Hades Chest", 100, 15, 'chest')
hadesLeggings = armor("Hades Leggings" , 100, 10, 'legging')
hadesBoots = armor("Hades Boots", 100, 5, 'boot')

Hades = mob('Hades' , 'greek' , 'death', 5, 225, [hadesHelm,hadesChest,hadesLeggings,hadesBoots], hadesBattleaxe)


#* regular mobs
skeleton = mob("Skeleton" , "death" , 'death' , 1 , 20 , [None] , dagger1)
zombie = mob("Zombie" , "death" , 'death' , 1 , 25 , [None] , gauntlet1)
demon = mob('demon' , "fire" , 'fire', 2, 40, [None], mace2)
waterElemental = mob('water elemental' , 'water' , 'water', 2, 40,[None],dagger2)
fireElemental = mob('fire elemental' , 'fire' , 'fire', 2, 40,[None],dagger2)



 #? how do i make mobs use ranged weapons

