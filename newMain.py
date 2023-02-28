import pygame
import pygame_gui
from drawHex import*
from Board import *
from TileResource import*
import math

#Initialise Pygame
def init_game():
    pygame.init()

#Screen size and other aesthetics
def setup_screen():
    screen_width, screen_height = 900, 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('The Settlers')
    window_surface = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.Surface((screen_width, screen_height))
    background.fill(pygame.Color('#9cd3db'))
    boardrect = pygame.Rect(100,100,800,600)
    return screen, window_surface, background, boardrect

#Quit button configuration
def setup_quit_button(screen_width, screen_height):
    quit_button_rect = pygame.Rect(screen_width - 110, screen_height - 60, 100, 50)
    quit_button_color = pygame.Color("red")
    font = pygame.font.Font(None, 36)
    return quit_button_rect, quit_button_color, font

#Texture configuration
def load_textures():
    desert = pygame.image.load("assets\Desert.png").convert_alpha() #120x140
    brick = pygame.image.load("assets\Brick.png").convert_alpha()
    grain = pygame.image.load("assets\Grain.png").convert_alpha()
    lumber = pygame.image.load("assets\Lumber.png").convert_alpha()
    ore = pygame.image.load("assets\Ore.png").convert_alpha()
    wool = pygame.image.load("assets\Wool.png").convert_alpha()
    testHex = pygame.image.load("assets\Hex.png").convert_alpha()
    return desert, brick, grain, lumber, ore, wool, testHex

#Function to match texture to value
def textureToVal(value):
    if value == TileResource.Brick:
        return brick
    elif value == TileResource.Nothing:
        return desert
    elif value == TileResource.Grain:
        return grain
    elif value == TileResource.Lumber:
        return lumber
    elif value == TileResource.Ore:
        return ore
    elif value == TileResource.Wool:
        return wool

#Draw vertices function
def drawVertices():
    for coord in testvert:
        if coord[2] == 'N':
            pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord[1],coord[0],110, 45),15,1)
        elif coord[2] == 'S':
            pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord[1],coord[0],110,190),15,1)

#Draw roads function
def drawRoads():
    for coord in testRoad:
        if coord[2] == 'W':
            pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord[1],coord[0],-15, 0),10)
        elif coord[2] == 'NW':
            pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord[1],coord[0],20,-50),10)
        else:
            pygame.draw.circle(background,'#000000',vertToPixel(75,coord[1],coord[0],70,-50),10)

#Draw hex function
def drawHexes():
    for coord in testboard:
        if testboard.get(coord) != None:
            background.blit(textureToVal(testboard[coord].resource), hexToPixel(75,coord[1],coord[0], 50))

#Main game loop
def run_game():
    clock = pygame.time.Clock()
    is_running = True
    
    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if quit_button_rect.collidepoint(mouse_pos):
                    is_running = False
                    pygame.quit()

        if pygame.display.get_active():
            window_surface.blit(background, (0, 0))
            #screen.blit(background, (0, 0))

            #Draw the Quit button
            pygame.draw.rect(screen, quit_button_color, quit_button_rect)
            quit_text = font.render("Quit", True, pygame.Color("white"))
            quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
            screen.blit(quit_text, quit_text_rect)

            #Update the display
            drawHexes()
            drawRoads()
            drawVertices()
            pygame.display.update()
            #clock.tick(time_delta)
    pygame.quit()

init_game()

#Screen
screen, window_surface, background, boardrect = setup_screen()
#Quit button configuration
quit_button_rect, quit_button_color, font = setup_quit_button(screen.get_width(), screen.get_height())
#Texture configuration
desert, brick, grain, lumber, ore, wool, testHex = load_textures()
if __name__ == "__main__":
    run_game()