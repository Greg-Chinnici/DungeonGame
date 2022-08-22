#! havent made any prices yet

#{name: boost} , names are not finalized
DungeonBoosts = {
    "Better Loot" : ["loot rarity ++"],
    "More Loot": ["loot cnt ++"],
    "Strong": ["weakens all enemies (even bosses)"]
}
DundgeonRunnerKits = {
    'Starter kit' = [[DungeonLootList[weapons][random.choice(range(3))]] , [DungeonLootList[armorKits][en(armorKits) % (len(armorKits) / 4)]] #pseudocode for picking the a random item from the weaapon list, number in the range will be from the rarity
#every type armor gets added to the kits
}
