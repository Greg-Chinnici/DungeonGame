#the numbers are just place holders 
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



weaponEnchants = {#it'll work when its in c#, this is just for concept and ideas
    "sharper": weapon.damage = weapon.damage * 1.5,#? will have multiple levels of sharpness
    "aware": weapon.range += 1,
    "hardened": weapon.durability += 300,
    "haste": weapon.attackSpeed *= 1.5, #? multple levls too?
    "vorpal": "higher crit chance" # i think crit chance should be tied to the player, armor can also increase this
}

rangedWeaponEnchants = {
    "pointy": "damage += 1",
    "piercing": "shoot thorugh multiple enemies",
    "super shot": "60 degree aoe shot"
}

allArmorEnchants = {
    "favored": "loot rarity += 1",
    "plentiful": "loot amount += 1",
    "hardened": "durability += 300",
    "scurvy": "loot rarity += 1 , loot amount -= 1"
}

legendaryEnchants = {
    "leech": "health steal from killed enemies", #no overheal
    "killshot": "one shot all basic enemies",
    "one of us": "invisable to enemies"#VERY RARE
}
