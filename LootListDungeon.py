#weapons and armor for dungeon game, will convert to C# later, or i could put it into a csv file. idk
#    https://www.fantasynamegenerators.com/dungeons-and-dragons.php 



#{name: [buffs]}
trophies = {#its no buff for now, some can be just aesthetic though
    "cup of demons blood": [None],
    "orc shahman's head": [None]
}
#{name: MobToFarm}
bossKeys = {#keys are very rare drops
    "Ares": ["any Greek them mob],
    "Neptune": ["any water type mob],
    "Wendigo": ["mobs killed at night / dark places"],
    "Yeti": ["any ice type mob"],
    "Loviatar": ["water type mobs],
    "Ogre King": ["chest loot"]
}

#{name: value}
coins = {"copper": 1,"silver": 5, "gold": 10}
#! loot will get better in the lists, higher index == stronger item
#{name: [durability, damage dealt, range, [attributes ("enchants will be  random")]]}
weapons = {
        "axe": [500, 10, 2, [None]],
        "sword": [300, 15, 1, [None]],
        "spear": [400, 8, 4, [None]]
        }#{name: [durability, damage dealt, range, rate of fire (per minute),[attributes ("enchants will be  random")]]}
rangedWeapons = {
        "bow": [500, 6, 10, 30 ,[None]],
        "crossbow": [300, 15, 1, 20 ,[None]],
        }
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
helmet = {
    
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
chesplate = {
    
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
legplate = {
    
}
#{name: [durabilty, armor protection, [attributes ("enchants will be  random")]]}
shoes = {
    
}
#{name: [effects]}
potions = {
    "minor healing": [None],
    "major healing": [None],
}
