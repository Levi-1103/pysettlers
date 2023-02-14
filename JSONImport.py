import json
from TileResource import *
def importBoardFile(filename):
    f = open(filename)

    storefile = json.load(f)

    f.close()


    boardData = []

    for x in storefile.values():
        boardData.append((TileResource(x[0]),x[1]))
    
    return boardData


print(importBoardFile("BeginnerBoard.json"))