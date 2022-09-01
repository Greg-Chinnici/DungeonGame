#this these are the possible items that a mob drops when it is kiled
types = [
    'death',
    'earth',
    'fire', 
    'ice',
    'lightning',
    'magic',
    'sand',
    'water',
    ]

themes = [
    'folklore',
    'greek',
    'historical',
    'medival',
    'pirate',
    'popCulture',
    'roman',
    'viking'
    ]

def sortLists():
    types.sort()
    themes.sort()

    for type in  types:
        print(f"\'{type}\',")

    for line in range(5):
        print('')
        
    for theme in  themes:
        print(f"\'{theme}\',")


coins = {"copper": 1,"silver": 5, "gold": 10}
GeneralLootTable = [coins] #isnt effected by type or theme


class key():
    def __init__(self , name , opensDoor , ):
        self.name = name
        self.opensDoor = opensDoor
    def printInfo(self):
        print(f"this key will open the {self.opensDoor}")

wedigoKey = key("Wendigo Key" , "Wendigo Forest")
hadesKey = key('Hades Key' , "depths of hell")
plutoKey = key('Pluto Key' , 'underworld lair')
helKey = key("Hel Key" , 'cabin of death')
apophisKey = key('Apophis Key' , "Apophis\' Snake Pit")
yetiKey = key("Yeti Key" , "Yeti Cave")
loviatarKey = key('Loviatar Key' , "Loviatar\'s Layer")
neptuneKey = key('Neptune Key' , "Atlantis Vault")#neptune isnt from atlantis but idc, cool name
aresKey = key('Ares Key' , "Ares\' War Room")
freyaKey = key('Freya Key' , 'Freya\'s Mansion')
odinKey = key('Odin Key' , 'Odin\'s Throne Room' )

class basicMobDrops():
    def __init__(self, name, value, itemType):
        self.name = name 
        self.value = value #in game currency
        self.itemType = itemType #weapon, potion ingrediant, crafting ingrident, collectable, gems

    def printInfo(self):
        print(f"{self.name}: value: {self.value} , type: {self.itemType} ")

TimeBasedLootTable = {
    'day' : [],
    'night': [wedigoKey]
}

TypeLootTable = {
    'death': [hadesKey , plutoKey , helKey, apophisKey],
    'earth': [],
    'fire': [freyaKey],
    'ice': [yetiKey],
    'lightning': [],
    'magic': [odinKey],
    'sand': [],
    'water': [loviatarKey, neptuneKey]
}
ThemeLootTable = {
    'egyptian': [apophisKey],
    'folklore': [],
    'greek': [aresKey , hadesKey],
    'historical': [],
    'medival': [],
    'pirate': [],
    'popCulture': [],
    'roman': [plutoKey],
    'viking': [helKey , odinKey]
}
