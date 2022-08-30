# Art style:
- isometric with voxels or 2d topdown. leaning towards isometric. pixel art / cell shading, similar to terraria
- [3d to pixel art render comp](https://www.youtube.com/watch?v=1FrIBkuq0ZI)

# Generation:
- Level Geometry >> Level Color / Theme >> Level Teir >> Level Loot >> Level Spawners >> Level Mobs >> Mob Weapons
- ***random skews can be done in python with random.triangular()***
# Basic concept: 
- calm and relaxing game or occasionally terrifying
- mostly looting, easy fights
- personal treasure room to store trophies and loot
- Cost currency to enter the dungeon
- Loot can be sold for a fixed price, so I need a vendor
- Boss rooms can be accessed with special keys (needs to be an intentional fight)
   - Bosses will be much harder 
- only way to leave a dungeon is an extraction eagle
- maybe add a gear crafting mechanic??
# Little details:
- Lots of inventory space / weight for extended runs in the dungeon
- loot will be dropped from mobs and found in chests
- The farther you go from the start == better loot, or loot just scales with playtime / level
- Lose everything If you die in the dungeon, maybe an insurance system???
- It’ll be like Tarakov and a Dungeon game combined
- To extract you will need to find or buy bird bait, a giant bird will pick you up	
- entry upgrades can be bought from the store (better loot, weaker enemies, more loot, special quests) 
- Maybe add seals that increase differnt room types and themes
# Player UI:
- FOV silder in settings
- Color saturation in settings
- health ,  stamina? , majika? (limit potion use) , 
- large inventory , sortable in multiple ways
- hotswap armor / weapons , (type, durability)
   
## Player movemnet:
- Walk in all directions (360)
- Dodge / slide in 45 degrees around player
- Strafe jitter is ok
   
# Types of Monsters:
- monsters are referred to as mobs in most of the code
- almost anything from any mythology
- dugeon could have themes that only allow certain mobs to spawn (greek mythologoy, asian folklore)
- custom loot tables for themed dungeons
- they can be accessed by finding a theme seal
- rooms in a regular dungeon will be themed randomly
## Boss Monsters:
- Bosses are a tier 5 mob
- They will ONLY spawn in boss rooms
- A boss room door will have a random chance to replace an room exit, each one is specific to the room type
- keys can be found from themed mob drops or themed loot

# Level generation: 
- (each level is its own screen, not continueous walking) #! not finalized
- Tile based generation [RPG genertator](https://donjon.bin.sh/)
- combine the outlines of multiple shapes, then distribute the room items (chests, loot, spawners)
- every room will have at least 3 exits 
- minimap will show the layout and room items
- it will pixelize the angles that are not in cardinal directions, making it possible to ad the walls and such to be right angles

## another option:
- generate shapes on a canvas (no arrays or grid)
- smash the shapes together to make one large polygon but maintain most edges
- once the shape is done, add the floor color, wall color , ridge color
- make some random dirty spots on the floor, dithering on the color of the wall
   
- OR use Cellular Automata, Preferred 
   - [Cellualr Automata cave generator](http://pixelenvy.ca/wa/ca_cave.html)
