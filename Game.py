from Board2 import *
from Player import *
import random
class Game:
    def __init__(self,playerNum = 3):
        self.board = Grid(7)
        self.board.defaultBoard()
        self.players = []
        for i in range(playerNum):
            self.players.append(Player(i))
        
    def buildSettlement(self,player,point):
        pass

    def buildRoad():
        pass

    def upgradeSettlement():
        pass

    def rollDice():
        return random.randint(2,12)
