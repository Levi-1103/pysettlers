from Road import *
from Building import *
from TileResource import *
class Tile:
    def __init__(self, resource: TileResource, rollNum):
        self.resource = resource
        self.rollNum = rollNum
        self.has_robber = False

    def returnNum(self):
        return self.rollNum
#store edges and verts in tile ???
#or have seperate dicts / lists for it
#possibly lists are better then can have  a list of lists
