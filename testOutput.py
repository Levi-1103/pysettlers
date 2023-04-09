import pygame
import pygame_gui
from drawHex import*
from Board2 import *
from TileResource import*
import math

pygame.init()

width = 1600
height = 900

pygame.display.set_caption('The Settlers')
window_surface = pygame.display.set_mode((width, height))

background = pygame.Surface((width, height))
background.fill(pygame.Color('#9cd3db'))

boardrect = pygame.Rect(100,100,800,600)

desert = pygame.image.load("assets\Desert.png").convert_alpha() #120x140
brick = pygame.image.load("assets\Brick.png").convert_alpha()
grain = pygame.image.load("assets\Grain.png").convert_alpha()
lumber = pygame.image.load("assets\Lumber.png").convert_alpha()
ore = pygame.image.load("assets\Ore.png").convert_alpha()
wool = pygame.image.load("assets\Wool.png").convert_alpha()
water = pygame.image.load("assets\Hex.png").convert_alpha()




def textureToVal(value):
    match value:
        case TileResource.Brick:
            return brick
        case TileResource.Desert:
            return desert
        case TileResource.Grain:
            return grain
        case TileResource.Lumber:
            return lumber
        case TileResource.Ore:
            return ore
        case TileResource.Wool:
            return wool
        

clock = pygame.time.Clock()
is_running = True

board = Grid(7)

board.defaultBoard()





# for coord in board:
#         if board.get(coord) != '':
#             background.blit(textureToVal(board[coord].resource), hexToPixel(75,coord.q,coord.r, 50))
#         else:
#             background.blit(desert, hexToPixel(75,coord[1],coord[0], 50))


skip = [
    Hex(0,0),
    Hex(0,1),
    Hex(2,0),
    Hex(1,0),
    Hex(1,1),
    Hex(0,2),

    Hex(6,4),
    Hex(6,5),
    Hex(5,5),
    Hex(6,6),
    Hex(5,6),
    Hex(4,6)
]

for coord in board.tiles:
    if coord not in skip:
        pass
    
    if board.tiles[coord] != 'Water':
       background.blit(textureToVal(board.tiles[coord].resource),hexToPixel(75,coord.q,coord.r, 50))
    elif coord not in skip and board.tiles[coord] == 'Water':
        background.blit(water, hexToPixel(75,coord.q,coord.r, 50))

for key in touches(Vertex(3,3,'N')):
    print(board.tiles.get(key).resource)

# background.blit(brick, hexToPixel(75,0,2, 50))

# for coord in board.vertices:
#     if coord.s == 'N':
#         pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord.q,coord.r,110, 45),15,1)
#     if coord.s == 'S':
#         pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord.q,coord.r,110,190),15,1)

# for coord in board.edges:
#     if coord.s == 'W':
#         pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord.q,coord.r,-15, 0),10)
#     if coord.s == 'NW':
#         pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord.q,coord.r,20,-50),10)
#     if coord.s == 'NE':
#         pygame.draw.circle(background,'#000000',vertToPixel(75,coord.q,coord.r,70,-50),10)




while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    
    
    for key in corners(Hex(3,3)):
        if key.s == 'N':
            pygame.draw.circle(background,'#FF0000',vertToPixel(75,key.q,key.r,110,45),15)
        if key.s == 'S':
            pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,key.q,key.r,110,190),15)

    


    

    window_surface.blit(background, (0, 0))
 

    pygame.display.update()




