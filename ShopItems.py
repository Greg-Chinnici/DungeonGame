#! havent made any prices yet
import random
#{name: boost} , names are not finalized
DungeonBoosts = {
    "Better Loot Mod" : [Level.tier == int(random.triangular(1,3,1.33))],
    "More Loot Mod": [Level.LootCnt == int(random.triangular(1,2,1.33))], #multiplies the amount of total loot drops
    "Strong Mod": ["weakens all enemies (even bosses)"]
}
DungeonRunnerKits = {
    'Starter kit' : [DungeonLootList[weapons][random.choice(range(3))]] , [DungeonLootList[armorKits][range(len(armorKits) % (len(armorKits) / 4))]] #pseudocode for picking the a random item from the weaapon list, number in the range will be from the rarity
#every type armor gets added to the kits
}
