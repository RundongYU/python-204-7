import random

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        #mapx used to width

    def isValid(self, map_x, map_y):
        if (map_x < 0 or map_x >= self.width or
            map_y < 0 or map_y >= self.height):
            return False
        return True

    def getMapIndex(self, x, y):
        x = 10
        y = 3
        return (x, y)
    
    #def setGridType(self, map_x, map_y, type):
        #self.map[map_y][map_x] = type

    def getLocation(self, map_x, map_y):
        return(map_x, map_y)

    def getRandomMapIndex(self): #for randomcase in map size

         map_x = random.randint(0, self.width-1)
         map_y = random.randint(0, self.height-1)
         return (map_x, map_y)

    def showPlant(self, x, y):
        int = None
        map_x, map_y = self.getMapIndex(x, y)
        map_x = 0 # in screen's left side
        if self.isValid(map_x, map_y):
            int = self.getLocation(map_x, map_y)
        return 

    def showZombies(self, x, y):
        int = None
        map_x, map_y = self.getMapIndex(x, y)
        map_x = 10 # # in screen's right side
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            int = self.getLocation(map_x, map_y)
        return