import pygame
from Board import Grid, Hex
from Player import *
from TileResource import TileResource
from drawHex import hexToPixel

pygame.init()

# Set up the Pygame screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Split Screen Demo")

# Set up the font
font = pygame.font.SysFont(None, 36)

#import textures
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
        
board = Grid(7)

board.defaultBoard()


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



# Set up the left rectangle
left_rect_width = screen_width // 4 * 3
left_rect_height = screen_height
left_rect = pygame.Surface((left_rect_width, left_rect_height))
left_rect.fill((150, 150, 255))
#left_text = font.render("Left Rectangle", True, (0, 0, 0))
#left_rect.blit(left_text, (left_rect_width // 2 - left_text.get_width() // 2, left_rect_height // 2 - left_text.get_height() // 2))

# Set up the right rectangle
right_rect_width = screen_width // 4
right_rect_height = screen_height
right_rect = pygame.Surface((right_rect_width, right_rect_height))
right_rect.fill((255, 255, 255))
#right_text = font.render("Right Rectangle", True, (0, 0, 0))
resources = ["brick", "lumber", "ore", "grain", "wool"]

board_tiles_rect = pygame.Surface((left_rect_width, left_rect_height), pygame.SRCALPHA)
board_tiles_rect.fill((255,255,255,0))

for coord in board.tiles:
    if coord not in skip:
        pass
    if board.tiles[coord] != 'Water':
       board_tiles_rect.blit(textureToVal(board.tiles[coord].resource),hexToPixel(75,coord.q,coord.r, 50))
    elif coord not in skip and board.tiles[coord] == 'Water':
        board_tiles_rect.blit(water, hexToPixel(75,coord.q,coord.r, 50))

p1 = Player("Levi","RED")

print(p1.resources.items())

def printResources(name,resources):

    x = screen_width - screen_width / 8 - 100  # Starting x position for the text
    y = screen_height - 800  # Starting y position for the text
    
    player_name = font.render(name,True, (0, 0, 0))
    screen.blit(player_name,(x, y - 50))

    for key, value in resources.items():
        key_str = str(key)  # convert the TileResource object to a string
        key_surface = font.render(key_str, True, (0, 0, 0))
        screen.blit(key_surface, (x, y))
        value_surface = font.render(str(value), True, (0, 0, 0))
        screen.blit(value_surface, (x + 150, y))
        y += key_surface.get_height() + 10  # Add some space between the text
    
#right_rect.blit(right_text, (right_rect_width // 2 - right_text.get_width() // 2, right_rect_height // 2 - right_text.get_height() // 2))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            p1.add_resource('sheep', 2)

    # Update game state

    # Draw the screen
    screen.blit(left_rect, (0, 0))
    screen.blit(right_rect, (left_rect_width, 0))
    left_rect.blit(board_tiles_rect,(-100,0))
    printResources(p1.name,p1.resources)

    pygame.display.update()
