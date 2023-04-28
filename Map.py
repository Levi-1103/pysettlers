import random
from TileResource import TileResource
from Tile import *


# generate list of resources
def tiles():
    tiles = []

    for i in range(4):
        tiles.append(TileResource.Lumber)
        tiles.append(TileResource.Grain)
        tiles.append(TileResource.Wool)

        if i < 3:
            tiles.append(TileResource.Brick)
            tiles.append(TileResource.Ore)

        if i == 0:
            continue
    tiles.append(TileResource.Desert)

    return tiles


# generate list of roll nums for resources
def tileNum():
    tileNums = []
    for i in range(3, 12):
        if i == 7:
            continue
        else:
            tileNums.append(i)
            tileNums.append(i)
    tileNums.append(2)
    tileNums.append(12)
    tileNums.append(7)

    return tileNums


# store tile and roll nums
hexRes = tiles()
hexNum = tileNum()

# add Empty tile to resource list
restest = random.sample(hexRes[:18], 18)
restest.append(TileResource.Desert)


# function for merging lists
def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


# new list of merged rolls and resources
new_board = merge(restest, hexNum)

# shuffle tiles for map
shuffle = random.sample(new_board, k=len(new_board))
