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
        self. anchorPoint = anchorPoint
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
        self. anchorPoint = anchorPoint
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

#how would I make a decahedron??????

TotalShapes = randint(20)
for shape in TotalShapes:
    shape = random.choice([shapes]) #! Not done

Square1 = Square(4)
Square2 = Square(3)
EqualiateralTriangle1 = EqualiateralTriangle(5 , False)
RightAngleTriangle1 = RightAngleTriangle(4, True)
shapes = [Square1 , Square2 , EqualiateralTriangle1 , RightAngleTriangle1]
def overlayShapes(shapes):
    for shape in shapes:
        #? how do i overlay them
