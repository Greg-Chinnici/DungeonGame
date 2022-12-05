import random

# 0 == blank , 1 == filled , 0.5 == right slope 45 degrees, -0.5 == left slope 45 degrees
MaxLevelSize = [100,100]
cols = MaxLevelSize[0] #x
rows = MaxLevelSize[1] #y
grid = [[[0] * cols] * rows]

#! i porbably dont even a grid, picture coudl br fine, just have no idea how i would edit a photo using only code

#* anchor points are defined as the top left forner box of the shape, NOT THE CENTER

#! i dont think it needs anchor points
#* each tile will be displayed as a 3x3 so it will actually be 300x300
#! could make it al inherit froma Shape class (similar variables)

'''
class Square():
    def __init__(self , sideLen , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchorPoint = anchorPoint #tuple
        self.square = [[[1] * sideLen] * sideLen]

    def newAnchorPoint(self):
        self.anchorPoint = (random.randint(0,self.sideLen),random.randint(0,self.sideLen))

class EqualiateralTriangle():
    def makeTriangle(sideLen):
        triangle = []
        for rowNum in range(sideLen):
            row = []
            row.append([0] * (sideLen - rowNum - 1)) #left side blank
            row.append([1] * (2 * rowNum + 1)) #filled spots
            row.append([0] * (sideLen - rowNum - 1)) #right side blank
            triangle.append(row)
        return triangle

    def __init__(self, sideLen, reverse , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchorPoint = anchorPoint
        triangle = makeTriangle(sideLen) #2d list output
        triangle = triangle.reverse() if reverse else triangle #flips verticle

class RightAngleTriangle():
    def makeTriangle(sideLen):
        triangle = []
        rowCnt = 1
        while rowCnt <= sideLen:
            row = [[1] * rowCnt]
            row.append([0] * (sideLen - rowCnt))
            triangle.append(row)
            rowCnt+=1
        return triangle

    def __init__(self , sideLen , reverse , anchorPoint = (0,0)):
        self.sideLen = sideLen
        self.anchorPoint = anchorPoint
        triangle = makeTriangle(sideLen) #2d list output
        triangle = triangle.reverse() if reverse else triangle


#? how would I make a decagon??????
class Octogon():
    def __init__(self , sideLen , anchorPoint = (0,0)):
        sideLenOne = [[0.5,1,-0.5],[1,1,1,1,1],[-0.5,1,0,5]]
        sideLenTwo = [[0,0.5,1,1,-0.5,0],[0.5,1,1,1,1,-0.5],[1,1,1,1,1,1],[1,1,1,1,1,1],[-0.5,1,1,1,1,0.5],[0,-0.5,1,1,0.5,0]]
        
        self.sideLen = sideLen 
        self.anchorPoint = anchorPoint
        self.octogon = sideLenOne if sideLen == 1 else sideLenTwo
    
'''

#* should ahvea access to the entire level grid
class ShapeBase():
    def __init__(self, anchorPoints, boundingBoxSize):
        self.m_anchorPoints = anchorPoints
        self.m_anchorPointx = anchorPoints[0]
        self.m_anchorPointx = anchorPoints[1]
        
        self.m_boundingBoxSize = boundingBoxSize
    
    def makeShape():
        pass
    
    def checkBounds(self):
        if self.m_anchorPointx - self.m_boundingBoxSize < 0:
            return False
        if self.m_anchorPointx + self.m_boundingBoxSize > 99:
            return False
        if self.m_anchorPointy - self.m_boundingBoxSize < 0:
            return False
        if self.m_anchorPointy + self.m_boundingBoxSize > 99:
            return False
        
        return True
        
class square(ShapeBase):
    def __init__(self, anchorPoints, boundingBoxSize):
        super().__init__(anchorPoints, boundingBoxSize)
    
    
   
    def makeShape(m_anchorPointx, m_anchorPointy , m_boundingBoxSize):
        def checkBounds(self):
            super().checkBounds()

        if not checkBounds():
            return
        
    
        for rowInShape in range(m_boundingBoxSize):
            for colInShape in range(m_boundingBoxSize):
                placeY = rowInShape + m_anchorPointy
                placeX = colInShape + m_anchorPointx
                
                grid[placeY][placeX] = '+' #if anchor point is top left of shape box 
    
            

class rightTriangleCornerBottomLeft(ShapeBase):
    def __init__(self, anchorPoints, boundingBoxSize):
        super().__init__(anchorPoints, boundingBoxSize)
        
    '''
    #+
    ##
    '''
    
    
   
    def makeShape(m_anchorPointx, m_anchorPointy , m_boundingBoxSize):
        def checkBounds(self):
            super().checkBounds()

        if not checkBounds():
            return
        
        for rowInShape in range(m_boundingBoxSize):
            for colInShape in range(m_boundingBoxSize):
                placeY = rowInShape + m_anchorPointy
                placeX = colInShape + m_anchorPointx
                
                if placeY >= placeX: #! fix th triangle rules
                    grid[placeY][placeX] = '+' #if right triangle corner in bottom left
            

class rightTriangleCornerBottomRight(ShapeBase):
    def __init__(self, anchorPoints, boundingBoxSize):
        super().__init__(anchorPoints, boundingBoxSize)
        
    '''
    ++#
    +##
    ###
    '''
    
    
   
    def makeShape(m_anchorPointx, m_anchorPointy , m_boundingBoxSize):
        def checkBounds(self):
            super().checkBounds()

        if not checkBounds():
            return
        
        for rowInShape in range(m_boundingBoxSize):
            for colInShape in range(m_boundingBoxSize):
                placeY = rowInShape + m_anchorPointy
                placeX = colInShape + m_anchorPointx
                
                if placeX >= placeY: #! fix th triangle rules
                    grid[placeY][placeX] = '+' #if right triangle corner in bottom left
            
class rightTriangleCornerTopRight(ShapeBase):
    def __init__(self, anchorPoints, boundingBoxSize):
        super().__init__(anchorPoints, boundingBoxSize)
    
    '''
    ##
    +#
    '''
   
    def makeShape(m_anchorPointx, m_anchorPointy , m_boundingBoxSize):
        def checkBounds(self):
            super().checkBounds()

        if not checkBounds():
            return
        
        colInShape = 0
        rowInShape = 0
        for rowInShape in range(m_boundingBoxSize):
            for colInShape in range(m_boundingBoxSize):
                placeY = rowInShape + m_anchorPointy
                placeX = colInShape + m_anchorPointx
                
                if placeY >= placeX: #! fix th triangle rules
                    grid[placeY][placeX] = '+' #if right triangle corner in bottom left
    
class rightTriangleCornerTopLeft(ShapeBase):
    def __init__(self, anchorPoints, boundingBoxSize):
        super().__init__(anchorPoints, boundingBoxSize)
    
    '''
    ##
    #+
    '''
   
    def makeShape(m_anchorPointx, m_anchorPointy , m_boundingBoxSize):
        def checkBounds(self):
            super().checkBounds()

        if not checkBounds():
            return
        
        colInShape = 0
        rowInShape = 0
        for rowInShape in range(m_boundingBoxSize):
            for colInShape in range(m_boundingBoxSize):
                placeY = rowInShape + m_anchorPointy
                placeX = colInShape + m_anchorPointx
                
                if placeY <= placeX: #! fix th triangle rules
                    grid[placeY][placeX] = '+' #if right triangle corner in bottom left
    
#* helpers

def printOutGrid():
    for row in grid:
        print(row)
        



'''
TotalShapes = int(random.triangular(5 , 25 , 17)) #25 max shapes, 17 avg shapes
shapes = []
for num in range(TotalShapes):
    shape = random.choice([Square(random.randint(1,5)) , EqualiateralTriangle(random.randint(1,7) , (random.randint(1,4) % 2 == 0)) , RightAngleTriangle(random.randint(1,7) , (random.randint(1,4) % 2 == 0)) , Octogon(random.randint(1,2))])
    shapes.append(shape)
'''