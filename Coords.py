#other option for making the grid uses list instead of dictionary
def initMap():
    q = 0
    r = 0


    map = [[ (q,r) for q in range(5)] for r in range(5)]

    map[0][0] = None
    map[1][0] = None
    map[0][1] = None
    map[4][3] = None
    map[3][4] = None
    map[4][4] = None

    
    
    return map

def printMap(map):
    for row in map:
        print(row)







