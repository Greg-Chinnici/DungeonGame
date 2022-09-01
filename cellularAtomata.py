import random
import math

height = 4
width = 4
grid = [range(height)*[range(width) * [0]]]

def firstFill():
    for lineIndex , line in enumerate(grid):
        for itemIndex , item in enumerate(line):
            grid[lineIndex][itemIndex] = random.randint(0,1)

def getWeight(lineIndex, itemIndex):
    #check the 8 surrouding items for their fill, 1 == wall  0 == floor
    weight = math.sum(grid[lineIndex-1][itemIndex-1], grid[lineIndex-1][itemIndex], grid[lineIndex-1][itemIndex+1], grid[lineIndex][itemIndex-1], grid[lineIndex][itemIndex+1], grid[lineIndex+1][itemIndex-1], grid[lineIndex+1][itemIndex],  grid[lineIndex][itemIndex+1])
    weight /= 4 #normalizes the average

    return weight

def newPass():
    workingGrid = [range(height)*[range(width) * [0]]]

    for lineIndex , line in enumerate(grid):
        for itemIndex , item in enumerate(line):
            if lineIndex == 0 or itemIndex == 0 or lineIndex == height-1 or itemIndex == width-1:
                pass
            else:
                workingGrid[lineIndex][itemIndex] = 1 if getWeight(lineIndex, itemIndex) > 1 else 0
    
    return workingGrid



firstFill()
passes = 3
for i in range(passes):
    grid = newPass()
    print(grid)