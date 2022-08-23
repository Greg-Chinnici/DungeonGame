#weapons and armor for dungeon game, will convert to C# later, or i could put it into a csv file. idk
#    https://www.fantasynamegenerators.com/dungeons-and-dragons.php 



#{name: [buffs]}
trophies = {#its no buff for now, some can be just aesthetic though
    "cup of demons blood": [None],
    "orc shahman's head": [None]
}
#{name: MobToFarm}
bossKeys = {#keys are very rare drops
    "Ares": ["any Greek them mob"],
    "Neptune": ["any water type mob"],
    "Wendigo": ["mobs killed at night / dark places"],
    "Yeti": ["any ice type mob"],
    "Loviatar": ["water type mobs"],
    "Ogre King": ["chest loot"]
}

#{name: value}
coins = {"copper": 1,"silver": 5, "gold": 10}
#! loot will get better in the lists, higher index == stronger item
#{name: [name, durability, damage, range, attackSpeed, type, attributes ("enchants will be  random")]}
weapons = {
    "Iron knife": [400 , 12 ,1 , 2 , "dagger", [None]],
    "Bronze knife": [500 , 16 ,1 , 3 , "dagger", [None]],
    "Steel knife": [600 , 20 ,2 , 4 , "dagger", [None]],
    "Iron Longsword": [500 , 14 ,2 , 0.5 , "longsword", [None]],
    "Bronze Longsword": [600 , 18 ,3 , 0.75 , "longsword", [None]],
    "Steel Longsword": [700 , 22 ,4 , 1 , "longsword", [None]],
    "Stone Axe": [500 , 15 ,2 , 1 , "handaxe", [None]],
    "Iron Axe": [700 , 18 ,2 , 1.25 , "handaxe", [None]],
    "Steel Axe": [800 , 21 ,2 , 1.5 , "handaxe", [None]],
    "Stone BattleaAxe": [700 , 18 ,2 , 0.33 , "battleaxe", [None]],
    "Iron BattleaAxe": [800 , 21 ,2 , 0.33 , "battleaxe", [None]],
    "Steel BattleaAxe": [950 , 23 ,3 , 0.33 , "battleaxe", [None]],
    "Iron Gauntlet": [400 , 20 ,1 , 0.5 , "gauntlet", [None]],
    "Bronze Gauntlet": [500 , 22 ,1 , 0.75 , "gauntlet", [None]],
    "Steel Gauntlet": [600 , 25 ,1 , 1 , "gauntlet", [None]],
    "Iron Mace": [500 , 10 ,1 , 1.33 , "mace", [None]],
    "Bronze Mace": [650 , 15 ,1 , 1.66 , "mace", [None]],
    "Steel Mace": [800 , 21 ,1 , 2 , "mace", [None]],
    "Iron Spear": [400 , 13 ,3 , 1 , "spear", [None]],
    "Steel Spear": [600 , 17 ,4 , 1.33 , "spear", [None]],
    "Diamond Spear": [800 , 22 ,5 , 1.66 , "spear", [None]]
        }#{name: [durability, arrow type , damage dealt, range, rate of fire (per minute),[attributes ("enchants will be  random")]]}
rangedWeapons = {
        "bow": [500, [None] ,6, 10, 30 ,[None]],
        "crossbow": [300, [None] ,15, 1, 20 ,[None]],
        }


#these will be combined into an array of player armor and thier stats will be combined
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
helmet = {
    "leather helm": [1000, 1, [None]],
    "chainmail helm": [1500, 2, [None]],
    "knights helm": [3000, 4, [None]]
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
chesplate = {
    "leather chesplate": [1000, 3, [None]],
    "chainmail chesplate": [1500, 4, [None]],
    "knights chesplate": [3000, 7, [None]]
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
legplate = {
    "leather legplate": [1000, 2, [None]],
    "chainmail braves": [1500, 3, [None]],
    "knights greaves": [3000, 6, [None]]
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
shoes = {
    "leather shoes": [1000, 1, [None]],
    "chainmail shoes": [1500, 3, [None]],
    "knights shoes": [3000, 5, [None]]
}
#{name: [effects]}
potions = {
    "minor healing": [None],
    "bird bait": ["spawns the bird"], #? should it be a potion or do I make a utility list?
    "major healing": [None],
}
