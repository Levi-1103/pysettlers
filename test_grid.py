from Board import *

test_board = Grid(7)

q = 1
r = 1


def test_neighbour():
    outcome = neighbours(Hex(q, q))

    assert outcome == [Hex(1, 2), Hex(2, 1), Hex(2, 0), Hex(1, 0), Hex(0, 1), Hex(0, 2)]


def test_borders():
    outcome = borders(Hex(q, q))

    assert outcome == [
        Edge(1, 1, "NE"),
        Edge(1, 1, "NW"),
        Edge(1, 1, "W"),
        Edge(0, 2, "NE"),
        Edge(1, 2, "NW"),
        Edge(2, 1, "W"),
    ]


def test_corners():
    outcome = corners(Hex(q, q))

    assert outcome == [
        Vertex(1, 1, "N"),
        Vertex(1, 0, "S"),
        Vertex(0, 2, "N"),
        Vertex(1, 1, "S"),
        Vertex(1, 2, "N"),
        Vertex(2, 0, "S"),
    ]


def test_joins_NE_Edge():
    outcome = joins(Edge(q, r, "NE"))

    assert outcome == [Hex(2, 0), Hex(1, 1)]


def test_joins_NW_Edge():
    outcome = joins(Edge(q, r, "NW"))

    assert outcome == [Hex(1, 1), Hex(1, 0)]


def test_joins_W_Edge():
    outcome = joins(Edge(q, r, "W"))

    assert outcome == [Hex(1, 1), Hex(0, 1)]


def test_endpoints_NE():
    outcome = endpoints(Edge(q, r, "NE"))

    assert outcome == [Vertex(2, 0, "S"), Vertex(1, 1, "N")]


def test_endpoints_NW():
    outcome = endpoints(Edge(q, r, "NW"))

    assert outcome == [Vertex(1, 1, "N"), Vertex(1, 0, "S")]


def test_endpoints_W():
    outcome = endpoints(Edge(q, r, "W"))

    assert outcome == [Vertex(1, 0, "S"), Vertex(0, 2, "N")]


def test_touches_N():
    outcome = touches(Vertex(q, r, "N"))

    assert outcome == [Hex(2, 0), Hex(1, 1), Hex(1, 0)]


def test_touches_S():
    outcome = touches(Vertex(q, r, "S"))

    assert outcome == [Hex(1, 1), Hex(1, 2), Hex(0, 2)]


def test_protrudes_N():
    outcome = protrudes(Vertex(q, r, "N"))

    assert outcome == [Edge(1, 1, "NE"), Edge(2, 0, "W"), Edge(1, 1, "NW")]


def test_protrudes_S():
    outcome = protrudes(Vertex(q, r, "S"))

    assert outcome == [Edge(1, 2, "NW"), Edge(0, 2, "NE"), Edge(1, 2, "W")]


def test_adjacent_N():
    outcome = adjacent(Vertex(q, r, "N"))

    assert outcome == [Vertex(2, -1, "S"), Vertex(1, 0, "S"), Vertex(2, 0, "S")]


def test_adjacent_S():
    outcome = adjacent(Vertex(q, r, "S"))

    assert outcome == [Vertex(0, 2, "N"), Vertex(0, 3, "N"), Vertex(1, 2, "N")]
