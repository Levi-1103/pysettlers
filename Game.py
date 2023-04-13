from Board import *
from Player import *
from Building import *
import random
class Game:
    def __init__(self,playerNum = 3,board_type = 'default'):
        self.board = Grid(7)
        if(board_type == 'default'):
            self.board.defaultBoard()
        else:
            #code for random board
            pass

        self.resource_cards = {}
        self.development_cards = {}

        self.players = []
        for i in range(playerNum):
            self.players.append(Player(i + 1,'RED'))

        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.current_turn = 0
        self.winner = None
        
    def start_game(self):

        self.current_turn = 1

        while not self.winner:
            print("Starting turn " + str(self.current_turn))
            print("Current player is  " + str(self.current_player.name))
            print(str(self.current_player.resources))


    def end_turn(self):
        current_player_index = (current_player_index + 1) % len(self.players)
        self.current_player = self.players[current_player_index]
        return self.current_player
    
    def roll_dice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        roll = dice1 + dice2
        print("Roll this turn", roll)
        #self.current_player.settlements for player settlements
        #check roll nums to settlements roll nums
        #if rollnums match assign resource to player

        
        for vert in self.board.vertices.keys():
            if self.board.vertices[vert] != '':
                print(touches(vert))
    
    def place_settlement(self,vertex,player):
        if self.board.vertices[vertex] == '':
            self.board.vertices.update({vertex: Building(BuildingType.Settlement,player)})
            player.add_settlement(vertex)


newgame = Game(4)

print(newgame.board.tiles.values())


def print_board(newgame):
    for tile in newgame.board.tiles.keys():
        if newgame.board.tiles[tile] != 'Water':
            for vert in corners(tile):
                if newgame.board.vertices[vert] !='':
                    print(vert)


newgame.place_settlement(Vertex(q=5, r=2, s='S'),newgame.current_player)

#print_board(newgame)

newgame.roll_dice()




        
        
