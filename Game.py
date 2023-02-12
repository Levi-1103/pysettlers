from Board import *
import Coords

map = Coords.initMap()




def popMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != None:
               map[i][j] = Hex(TileResource.Brick,5)


popMap(map)

def tileInfo(coords):
    return coords.resource ,coords.roll

print(tileInfo(map[2][1]))