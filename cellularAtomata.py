import random
import math

height = 5
width = 5
grid = [[0] * width] * height

def firstFill():
    for rowIndex , row in enumerate(grid):
        for itemIndex , item in enumerate(row):
            grid[rowIndex][itemIndex] = random.randint(0,1)

def sumNum(listOfNums):
    sum = 0
    for n in listOfNums:
        sum += n
    return sum

def getWeight(lineIndex, itemIndex, grid):
    #check the 8 surrouding items for their fill, 1 == wall  0 == floor
    weight = sumNum([grid[lineIndex-1][itemIndex-1], grid[lineIndex-1][itemIndex], grid[lineIndex-1][itemIndex+1], grid[lineIndex][itemIndex-1], grid[lineIndex][itemIndex+1], grid[lineIndex+1][itemIndex-1], grid[lineIndex+1][itemIndex],  grid[lineIndex][itemIndex+1]])
    weight /= 4 #normalizes the average
    print(weight)
    return weight

def newPass(grid):
    workingGrid = [[0] * width] * height

    for lineIndex , line in enumerate(grid):
        for itemIndex , item in enumerate(line):
            if lineIndex == 0 or itemIndex == 0 or lineIndex == height-1 or itemIndex == width-1:
                print(item)
            else: #! not working
                workingGrid[lineIndex][itemIndex] = 1 if getWeight(lineIndex, itemIndex, grid) < 1 else 0
    return workingGrid


firstFill()
for line in grid:
        print(line , "\n")

passes = 1
for i in range(passes):
    grid = newPass(grid)
    print(grid)