
#could also make the walls differnt depinding on the color, (brick mortar chnage, vines, cracks, )
#floor will be dotted with the wall color randomly
class Level():
    def __init__(self, floorColor, ridgeColor, wallColor, tier):
        self.floorColor = floorColor
        self.ridgeColor = ridgeColor
        self.wallColor = wallColor
        self.tier = tier

    def generateGeometry():
        #still deciding how to make the levels
    
    def spawnEnemies():
        placeEnemy(mob(tier))
    
    spawnLoot(tier)
    
    enterLevel(player)
    

#rgb, tempory for now, just showing that I want to make custom colored rooms (within reason)
RED = [255,0,0]
CRIMSON = [220,20,60]
MAROON = [128,0,0]
SALMON = [250,128,114]

ORANGE = [255,165,0]
DARKORANGE = [255,140,0]
TAN = [210,180,140]
PERU = [205,133,63]

YELLOW = [255,255,102]
KHAKI = [240,230,140]
LIGHTSAND = [255,235,205]

GREEN = [0,128,0]
LAWNGREEN = [124,252,0]
MEDIUMSEAGREEN = [60,179,113]
SEAGREEN = [46,139,87]
DARKCYAN = [0,139,139]

BLUE = [0,0,255]
POWDERBLUE = [176,224,230]
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
SeaTheme = Level(POWDERBLUE , DARKCYAN , NAVY, 1)
