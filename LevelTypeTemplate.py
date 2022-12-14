
#could also make the walls differnt depinding on the color, (brick mortar change, vines, cracks)
import random

#the floor color will determine the type / theme. Types : water, fire, ice, earth, lightning. Themes: Greek, Roman, folklore.  Some mobs (grunts) can be used in multiple rooms just change the loot table per room to be effected by the tier if mob killed
#* when placing the floor colors i can sloghtly change a small amount of tiles in their rgb values to make more detail
class Level():
    def __init__(self, floorColor, ridgeColor, wallColor, tier):
        self.floorColor = floorColor
        self.ridgeColor = ridgeColor
        self.wallColor = wallColor
        self.tier = tier
        self.LevelShape = generateGeometry() #2d list?
        self.gridXlen = len(self.LevelShape[0])
        self.gridYLen = len(self.LevelShape)
    def generateGeometry(self):
        pass
        #still deciding how to make the levels
    def fillcolor(self):
        for pixel in self.LevelShape:
            shade = self.floorColor if random.randint(100) < 80 else (self.floorColor[1] += random.randint(-10, 10))# random shading
            pixel = shade
    def generateLoot(self):
        lootCnt = random.triangular(1 , 10 , self.tier * 2)
        possibleLootLocations = []
        for loot in range(lootCnt): #check for possible spots
            for col in range(self.gridXLen):
                for row in range(self.gridYLen):
                    if self.LevelShape[col][row] == 1: #if it is the floor 
                        possibleLootLocations.append((col , row)) #tuple of the coordiante of posible spot
        lootLocations = random.choices(possibleLootLocations , None , None , lootCnt)
        for location in lootLocations:
            spawnLoot(location)
    

        
    def spawnEnemies():
        placeEnemy(mob(tier))
    
    generateLoot(self)
    
    enterLevel(player)

class BossLevel():
    def __init__(self, floorColor, ridgeColor, wallColor):
        self.floorColor = floorColor
        self.ridgeColor = ridgeColor
        self.wallColor = wallColor
        self.tier = 5
        self.LevelShape = generateGeometry() #2d list?
    
    
    def generateGeometry(self):
        pass
        #still deciding how to make the levels
    
    def generateLoot(self):
        lootCnt = random.triangular(1 , 10 , self.tier * 2)
        possibleLootLocations = []
        for loot in range(lootCnt): #check for possible spots
            for col in range(gridXLen):
                for row in range(gridYLen):
                    if grid[col][row] == 1: #if it is the floor 
                        possibleLootLocations.append((col , row)) #tuple of the coordiante of posible spot
        lootLocations = random.choices(possibleLootLocations , None , None , lootCnt)
        for location in lootLocations:
            spawnLoot(location)
    
#rgb, tempory for now, just showing that I want to make custom colored rooms (within reason), these are all constants
WHITE = [255,255,255]

RED = [255,0,0]
CRIMSON = [220,20,60]
MAROON = [128,0,0]
SALMON = [250,128,114]

ORANGE = [255,165,0]
DARKORANGE = [255,140,0]
TAN = [210,180,140]
PERU = [205,133,63]

YELLOW = [255,255,102]
BLANCHEDALMOND = [255,235,205]
BEIGE = [245,245,220]
BURLYWOOD = [222,184,135]
KHAKI = [240,230,140]

GREEN = [0,128,0]
LAWNGREEN = [124,252,0]
MEDIUMSEAGREEN = [60,179,113]
SEAGREEN = [46,139,87]
DARKCYAN = [0,139,139]

BLUE = [0,0,255]
LIGHTBLUE = [173,216,230]
CADETBLUE = [95,158,160]
NAVY = [0,0,128]
STEELBLUE = [70,130,180]
SLATEBLUE = [106,90,205]

PURPLE = [128,0,128]
BLUEPURPLE = [138,43,226]

BLACK = [0,0,0]
GREY = [128,128,128]
SILVER = [192,192,192]
LIGHTGREY = [211,211,211]



DesertTheme = Level(YELLOW , ORANGE , PERU , 2)
DarkTheme = Level(LIGHTGREY , GREY , BLACK , 1)
GardenTheme = Level(LAWNGREEN , SEAGREEN , DARKCYAN , 3)
EvilTheme = Level(SLATEBLUE , LIGHTGREY , GREY , 3)
MagicTheme = Level(BLUEPURPLE , SILVER , BLACK , 1)
LightningTheme = Level(CADETBLUE , YELLOW ,  BLUEPURPLE, 2)

GeneralDayTheme = Level(GREEN , STEELBLUE , GREY, 1)
GeneralNightTheme = Level(CADETBLUE , NAVY ,  BLUEPURPLE, 1)

DeathBossRoom = BossLevel(SLATEBLUE , BLACK , LIGHTGREY)
FireBossRoom = BossLevel(ORANGE , RED , BEIGE)
IceBossRoom = BossLevel(LIGHTBLUE , WHITE , CADETBLUE)
WaterBossRoom = BossLevel(BLUE , STEELBLUE , NAVY)

VikingBossRoom = BossLevel(BEIGE , KHAKI , PERU)
GreekBossRoom = BossLevel(WHITE , GREY , BEIGE)