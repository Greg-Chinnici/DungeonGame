# Art style:
  isometric with voxels or 2d topdown. leaning towards isometric. pixel art / cell shading, similar to terraria
  [3d to pixel art render comp](https://www.youtube.com/watch?v=1FrIBkuq0ZI)

# H1 Generation:
   Level Geometry >> Level Color / Theme >> Level Teir >> Level Loot >> Level Spawners >> Level Mobs >> Mob Weapons
   ***random skews can be done in pythin with random.triangular()
# Basic concept: 
   calm and relaxing game or occasionally terrifying
   mostly looting, easy fights
   personal treasure room to store trophies and loot
   Cost currency to enter the dungeon
   Loot can be sold for a fixed price, so I need a vendor
    oss rooms can be accessed with special keys (needs to be an intentional fight)
       Bosses will be much harder 
    only way to leave a dungeon is an extraction eagle
    maybe add a gear crafting mechanic??
# Little details:
   Lots of inventory space / weight for extended runs in the dungeon
   loot will be dropped from mobs and found in chests
   The farther you go from the start == better loot, or loot just scales with playtime / level
   Lose everything If you die in the dungeon, maybe an insurance system???
   It’ll be like Tarakov and a Dungeon game combined
   To extract you will need to find or buy bird bait, a giant bird will pick you up	
   entry upgrades can be bought from the store (better loot, weaker enemies, more loot, special quests) 
# Player UI:
   FOV silder in settings
   Color saturation in settings
   health ,  stamina? , majika? (limit potion use) , 
   large inventory , sortable in multiple ways
   hotswap armor / weapons , (type, durability)
    
# Types of Monsters:
   almost anything from any mythology
   dugeon could have themes that only allow certain mobs to spawn (greek mythologoy, asian folklore)
   custom loot tables for themed dungeons
   they can eb accessed by finding a theme seal
   rooms in a regular dungeon will be themed randomly
# Level generation: 
   (each level is its own screen, not continueous walking) #! not finalized
   Tile based generation
   [RPG genertator](https://donjon.bin.sh/)
   combine the outlines of multiple shapes, then distribute the room items (chests, loot, spawners)
   every room will have at least 3 exits 
   minimap will show the layout and room items
    
   it will pixelize the angles that are not in cardinal directions, making it possible to ad the walls and such to be right angles
    
   OR use Cellular Automata, Preferred 
       [Cellualr Automata cave generator](http://pixelenvy.ca/wa/ca_cave.html)
