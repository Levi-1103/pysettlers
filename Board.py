from collections import namedtuple
from Tile import *
from Map import *

Hex = namedtuple("Hex", "q r")
Vertex = namedtuple("Vertex", "q r s")
Edge = namedtuple("Edge", "q r s")


class Grid:
    '''Class for creating a hexagon grid'''
    def __init__(self, size):
        self.tiles = {}
        self.edges = {}
        self.vertices = {}
        size

        for q in range(size):
            for r in range(size):
                self.tiles.update({Hex(q, r): "Water"})
                self.edges.update({Edge(q, r, "NE"): ""})
                self.edges.update({Edge(q, r, "NW"): ""})
                self.edges.update({Edge(q, r, "W"): ""})
                self.vertices.update({Vertex(q, r, "N"): ""})
                self.vertices.update({Vertex(q, r, "S"): ""})

    def defaultBoard(self):
        """Populates the Game Board with the Catan Starter Board"""
        # 1st Row
        self.tiles.update({Hex(3, 1): Tile(TileResource.Ore, 10)})
        self.tiles.update({Hex(4, 1): Tile(TileResource.Wool, 2)})
        self.tiles.update({Hex(5, 1): Tile(TileResource.Lumber, 9)})
        # 2nd Row
        self.tiles.update({Hex(2, 2): Tile(TileResource.Grain, 12)})
        self.tiles.update({Hex(3, 2): Tile(TileResource.Brick, 6)})
        self.tiles.update({Hex(4, 2): Tile(TileResource.Wool, 4)})
        self.tiles.update({Hex(5, 2): Tile(TileResource.Brick, 10)})

        # 3rd Row
        self.tiles.update({Hex(1, 3): Tile(TileResource.Grain, 9)})
        self.tiles.update({Hex(2, 3): Tile(TileResource.Lumber, 11)})
        self.tiles.update({Hex(3, 3): Tile(TileResource.Desert, 7)})
        self.tiles.update({Hex(4, 3): Tile(TileResource.Lumber, 3)})
        self.tiles.update({Hex(5, 3): Tile(TileResource.Ore, 8)})
        # 4th Row
        self.tiles.update({Hex(1, 4): Tile(TileResource.Lumber, 8)})
        self.tiles.update({Hex(2, 4): Tile(TileResource.Ore, 3)})
        self.tiles.update({Hex(3, 4): Tile(TileResource.Grain, 4)})
        self.tiles.update({Hex(4, 4): Tile(TileResource.Wool, 5)})
        # 5th Row
        self.tiles.update({Hex(1, 5): Tile(TileResource.Brick, 5)})
        self.tiles.update({Hex(2, 5): Tile(TileResource.Grain, 6)})
        self.tiles.update({Hex(3, 5): Tile(TileResource.Wool, 11)})

        # code to delete empty tiles

    def random_board(self):
        """Populates the Board with Random tiles that are generated in Map.py"""
        self.tiles.update({Hex(3, 1): Tile(*shuffle[0])})
        self.tiles.update({Hex(4, 1): Tile(*shuffle[1])})
        self.tiles.update({Hex(5, 1): Tile(*shuffle[2])})
        # 2nd Row
        self.tiles.update({Hex(2, 2): Tile(*shuffle[3])})
        self.tiles.update({Hex(3, 2): Tile(*shuffle[4])})
        self.tiles.update({Hex(4, 2): Tile(*shuffle[5])})
        self.tiles.update({Hex(5, 2): Tile(*shuffle[6])})

        # 3rd Row
        self.tiles.update({Hex(1, 3): Tile(*shuffle[7])})
        self.tiles.update({Hex(2, 3): Tile(*shuffle[8])})
        self.tiles.update({Hex(3, 3): Tile(*shuffle[9])})
        self.tiles.update({Hex(4, 3): Tile(*shuffle[10])})
        self.tiles.update({Hex(5, 3): Tile(*shuffle[11])})
        # 4th Row
        self.tiles.update({Hex(1, 4): Tile(*shuffle[12])})
        self.tiles.update({Hex(2, 4): Tile(*shuffle[13])})
        self.tiles.update({Hex(3, 4): Tile(*shuffle[14])})
        self.tiles.update({Hex(4, 4): Tile(*shuffle[15])})
        # 5th Row
        self.tiles.update({Hex(1, 5): Tile(*shuffle[16])})
        self.tiles.update({Hex(2, 5): Tile(*shuffle[17])})
        self.tiles.update({Hex(3, 5): Tile(*shuffle[18])})


def neighbours(tile):
    """
    Returns neighbouring tiles based on an input Tile
    """
    q = tile.q
    r = tile.r
    return [
        Hex(q, r + 1),
        Hex(q + 1, r),
        Hex(q + 1, r - 1),
        Hex(q, r - 1),
        Hex(q - 1, r),
        Hex(q - 1, r + 1),
    ]


def borders(tile):
    q = tile.q
    r = tile.r
    return [
        Edge(q, r, "NE"),
        Edge(q, r, "NW"),
        Edge(q, r, "W"),
        Edge(q - 1, r + 1, "NE"),
        Edge(q, r + 1, "NW"),
        Edge(q + 1, r, "W"),
    ]


def corners(tile):
    q = tile.q
    r = tile.r

    return [
        Vertex(q, r, "N"),
        Vertex(q, r - 1, "S"),
        Vertex(q - 1, r + 1, "N"),
        Vertex(q, r, "S"),
        Vertex(q, r + 1, "N"),
        Vertex(q + 1, r - 1, "S"),
    ]


def joins(edge):
    (q, r, s) = edge

    if s == "NE":
        return [Hex(q + 1, r - 1), Hex(q, r)]
    elif s == "NW":
        return [Hex(q, r), Hex(q, r - 1)]
    elif s == "W":
        return [Hex(q, r), Hex(q - 1, r)]


def endpoints(edge):
    (q, r, s) = edge
    if s == "NE":
        return [Vertex(q + 1, r - 1, "S"), Vertex(q, r, "N")]
    elif s == "NW":
        return [Vertex(q, r, "N"), Vertex(q, r - 1, "S")]
    elif s == "W":
        return [Vertex(q, r - 1, "S"), Vertex(q - 1, r + 1, "N")]


def touches(vertex):
    q = vertex.q
    r = vertex.r
    s = vertex.s

    if s == "N":
        return [Hex(q + 1, r - 1), Hex(q, r), Hex(q, r - 1)]
    if s == "S":
        return [Hex(q, r), Hex(q, r + 1), Hex(q - 1, r + 1)]


def protrudes(vertex):
    (q, r, s) = vertex
    if s == "N":
        return [Edge(q, r, "NE"), Edge(q + 1, r - 1, "W"), Edge(q, r, "NW")]
    if s == "S":
        return [Edge(q, r + 1, "NW"), Edge(q - 1, r + 1, "NE"), Edge(q, r + 1, "W")]


def adjacent(vertex):
    (q, r, s) = vertex
    if s == "N":
        return [
            Vertex(q + 1, r - 2, "S"),
            Vertex(q, r - 1, "S"),
            Vertex(q + 1, r - 1, "S"),
        ]
    if s == "S":
        return [
            Vertex(q - 1, r + 1, "N"),
            Vertex(q - 1, r + 2, "N"),
            Vertex(q, r + 1, "N"),
        ]
