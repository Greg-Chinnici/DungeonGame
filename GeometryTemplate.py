# 0 == blank , 1 == filled

from random import triangular


cols = 20 #x
rows = 20 #y
grid = [[[0]*cols]*rows]

class Square():
    def __init__(self , sideLen , anchorPoint):
        self.sideLen = sideLen
        self.anchoirPOint = anchorPoint
        square = [[[1]*sideLen]*sideLen]
        
class EqualiateralTriangle():
    def __init__(self, sideLen, anchorPoint, reverse):
        self.sideLen = sideLen
        self. anchorPoint = anchorPoint
        triangle = makeTriangle(sideLen) #2d list output
        triangle = triangle.reverse() if reverse else triangle
    
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
    def __init__(self , sideLen , anchorPoint, reverse):
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