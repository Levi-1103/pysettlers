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
