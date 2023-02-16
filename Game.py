from BoardList import *
import Coords

map = Coords.initMap()
hexRes = tiles()
hexNum = tileNum()

hexNum.append(7)

def popMap(map,res,num):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != None:
                print('test')
                map[i][j] = Hex(res.pop(),num.pop())


popMap(map,hexRes,hexNum)

def tileInfo(coords):
    return coords.resource ,coords.roll

print(tileInfo(map[2][1]))

print(tileInfo(map[2][0]))
print(tileInfo(map[3][0]))

# print(len(hexNum))
# print(len((hexRes)))

#generate 18 hexes and nums and add to list
#add desert tile with roll 7  at end of list
# shuffle list
#populate map with list

#possibly change list to hashmap
#iterate through dict of edges check if it has owner
# if its owned by a player add to point total

#main game class that will be created when game is started
#store game data which later than can be saved and reloaded

#correlate points grid to hex height
#add default sprites marking empty spot
#add code for changi sprite to different icon when clicked
#store points in dict in fomrat (q,r,N/S)
#if N add to coord if S minus??

#use named tuple for coords in dict ??

