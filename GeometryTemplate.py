import random
# 0 == blank , 1 == filled
MaxLevelSize = [100,100]
cols = MaxLevelSize[0] #x
rows = MaxLevelSize[1] #y
grid = [[[0] * cols] * rows]

#! could make it al inherit froma Shape class (similar variables)
class Square():
    def __init__(self , sideLen , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchoirPOint = anchorPoint #tuple
        square = [[[1] * sideLen] * sideLen]

class EqualiateralTriangle():
    def __init__(self, sideLen, reverse , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchorPoint = anchorPoint
        triangle = makeTriangle(sideLen) #2d list output
        triangle = triangle.reverse() if reverse else triangle #flips verticle

    def makeTriangle(sideLen):
        triangle = []
        for rowNum in range(sideLen):
            row = []
            row.append([0] * (sideLen - rowNum - 1)) #left side blank
            row.append([1] * (2 * rowNum + 1)) #filled spots
            row.append([0] * (sideLen - rowNum - 1)) #right side blank
            triangle.append(row)
        return triangle

class RightAngleTriangle():
    def __init__(self , sideLen , reverse , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchorPoint = anchorPoint
        triangle = makeTriangle(sideLen) #2d list output
        triangle = triangle.reverse() if reverse else triangle

    def makeTriangle(sideLen):
        triangle = []
        rowCnt = 1
        while rowCnt <= sideLen:
            row = [[1] * rowCnt]
            row.append([0] * (sideLen - rowCnt))
            triangle.append(row)
            rowCnt+=1
        return triangle

#? how would I make a decahedron??????

TotalShapes = int(random.triangular(5 , 25 , 17)) #25 max shapes, 17 avg shapes
shapes = []
for shape in range(TotalShapes):
    shape = random.choice([Square(random.randint(0,5)) , EqualiateralTriangle(random.randint(0,7) , (random.randint(0,4) % 2 == 0)) , RightAngleTriangle(random.randint(0,7) , (random.randint(0,4) % 2 == 0))])
    shapes.append(shape)

for shape in shapes:
    print(type(shape))
