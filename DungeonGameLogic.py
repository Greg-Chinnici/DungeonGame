#gameloop
'''
rooms will be stored after the player leves them so they will retain thier state if the player wants to go back 
'''

#i might want to make it change based on a radius from  the  spawn room
health = 20
roomsEntered = 0 #this will be the seed for the increased loot rarity
while health > 0:
    if isInExitDoor(player):
        makeNewRoom(roomsEntered)#genreates a new room and teleports the player into it, also makes chest and other room addOns 
        roomsEntered += 1
    
    if getEscapeEagle(player):
        spawnEagle() #escape eaglew spawns and picks up the player, there is a 30 second delay so you cant combat log
#when rhe player dies

goBackToBase(player) #teleports the player to home base if they die, and clears inventory
