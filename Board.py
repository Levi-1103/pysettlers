
import random

from TileResource import TileResource


class Board():
    def __init__(self, game):
        self.game = game

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
                tiles.append(TileResource.Nothing)
        random.shuffle(tiles)

        return tiles

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

        random.shuffle(tileNums)
        return tileNums

    hexRes = tiles()
    hexNum = tileNum()


class Hex:
    def __init__(self, resource, roll):
        self.resource = resource
        self.roll = roll


class Edge:
    def __init__(self, hasRoad, owner):
        self.hasRoad = hasRoad
        self.owner = owner


class Vertex:
    def _init_(self, hasBuilding, buildingType, owner):
        self.hasBuilding = hasBuilding
        self.buildingType = buildingType
        self.owner = owner


# print(Board.tiles())
# print(len(Board.tiles()))
# print(Board.tileNum())
# print(len(Board.tileNum()))

# newgame = Board(game='')


# hex1 = Hex(newgame.hexRes.pop(), newgame.hexNum.pop())

# print(hex1.resource)
# print(hex1.roll)

