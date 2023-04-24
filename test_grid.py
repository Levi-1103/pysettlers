from Board import *

test_board = Grid(7)

q = 1
r = 1

def test_neighbour():
    outcome = neighbours(Hex(q,q))

    assert outcome == [
        Hex(1, 2),
        Hex(2, 1),
        Hex(2, 0),
        Hex(1, 0),
        Hex(0, 1),
        Hex(0, 2)
    ]

def test_borders():
    outcome = borders(Hex(q,q))

    assert outcome == [
        Edge(q, r, 'NE'),
        Edge(q, r, 'NW'),
        Edge(q, r, 'W'),
        Edge(q-1, r+1, 'NE'),
        Edge(q, r+1, 'NW'),
        Edge(q+1, r, 'W')
    ]


def test_corners():
    outcome = corners(Hex(q,q))

    assert outcome == [
        Vertex(q, r, 'N'),
        Vertex(q, r-1, 'S'),
        Vertex(q-1, r+1, 'N'),
        Vertex(q, r, 'S'),
        Vertex(q, r+1, 'N'),
        Vertex(q+1, r-1, 'S')
    ]

def test_joins_NE_Edge():
    outcome = joins(Edge(q,r,'NE'))
    
    assert outcome == [
            Hex(q + 1, r - 1),
            Hex(q, r)
        ]
    
def test_joins_NW_Edge():
    outcome = joins(Edge(q,r,'NW'))
    
    assert outcome == [
            Hex(q, r),
            Hex(q, r - 1)
        ]
    
def test_joins_W_Edge():
    outcome = joins(Edge(q,r,'W'))
    
    assert outcome == [
            Hex(q, r),
            Hex(q, r - 1)
        ]



def test_endpoints_NE():
    outcome = endpoints(Edge(q,r,'NE'))
    
    assert outcome == [
            Vertex(q + 1, r - 1, 'S'),
            Vertex(q, r, 'N')
        ]

def test_endpoints_NW():
    outcome = endpoints(Edge(q,r,'NW'))
    
    assert outcome == [
            Vertex(q, r, 'N'),
            Vertex(q, r - 1, 'S')
        ]
    
def test_endpoints_W():
    outcome = endpoints(Edge(q,r,'W'))
    
    assert outcome == [
            Hex(q, r - 1, 'S'),
            Hex(q - 1, r + 1, 'N')
        ]


def test_touches():
    pass

def test_protrudes():
    pass


def test_adjacent():
    pass

