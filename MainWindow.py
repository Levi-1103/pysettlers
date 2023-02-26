import pygame
import pygame_gui
from drawHex import*
from Board import *
from TileResource import*
import math

def start_game():
    #initialise pygame
    pygame.init()

    #screen size and other aesthetics
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('The Settlers')
    window_surface = pygame.display.set_mode((screen_width, screen_height))

    background = pygame.Surface((screen_width, screen_height))
    background.fill(pygame.Color('#9cd3db'))
    font = pygame.font.Font(None, 36)
    boardrect = pygame.Rect(100,100,800,600)

    #Quit button creation
    quit_button_screen_width = 100
    quit_button_screen_height = 50
    quit_button_rect = pygame.Rect(
        screen_width - quit_button_screen_width - 10,
        screen_height - quit_button_screen_height - 10,
        quit_button_screen_width,
        quit_button_screen_height,
    )
    quit_button_color = pygame.Color("red")
    # manager = pygame_gui.UIManager((screen_width, screen_height))

    # new_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 480), (100, 50)), text='New Game', manager=manager)

    # settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 480), (100, 50)), text='Settings', manager=manager)

    # quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 480), (100, 50)), text='Quit', manager=manager)

    #minimize_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 50)), text='_', manager=manager)

    #credits_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 50)), text='Credits', manager=manager)

    #textures
    desert = pygame.image.load("assets\Desert.png").convert_alpha() #120x140
    brick = pygame.image.load("assets\Brick.png").convert_alpha()
    grain = pygame.image.load("assets\Grain.png").convert_alpha()
    lumber = pygame.image.load("assets\Lumber.png").convert_alpha()
    ore = pygame.image.load("assets\Ore.png").convert_alpha()
    wool = pygame.image.load("assets\Wool.png").convert_alpha()

    testHex = pygame.image.load("assets\Hex.png").convert_alpha()

    def textureToVal(value):
        match value:
            case TileResource.Brick:
                return brick
            case TileResource.Nothing:
                return desert
            case TileResource.Grain:
                return grain
            case TileResource.Lumber:
                return lumber
            case TileResource.Ore:
                return ore
            case TileResource.Wool:
                return wool
            





    for coord in testboard:
            if testboard.get(coord) != None:
                background.blit(textureToVal(testboard[coord].resource), hexToPixel(75,coord[1],coord[0], 50))

    # for coord in testboard:
    #         if testboard.get(coord) != None:
    #          background.blit(testHex, hexToPixel(75,coord[1],coord[0], 50))

    # for coord in testboard:
    #     background.blit(testHex, hexToPixel(75,coord[1],coord[0], 50))
            

    for coord in testvert:
        print(coord[2])
        if coord[2] == 'N':
            pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord[1],coord[0],110, 45),15,1)
        if coord[2] == 'S':
            pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord[1],coord[0],110,190),15,1)

    for coord in testRoad:
        print(coord[2])
        if coord[2] == 'W':
            pygame.draw.circle(background,'#FF0000',vertToPixel(75,coord[1],coord[0],-15, 0),10)
        if coord[2] == 'NW':
            pygame.draw.circle(background,'#FFFFFF',vertToPixel(75,coord[1],coord[0],20,-50),10)
        if coord[2] == 'NE':
            pygame.draw.circle(background,'#000000',vertToPixel(75,coord[1],coord[0],70,-50),10)
            

    #main game loop
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

        # Draw the Quit button
        pygame.draw.rect(screen, quit_button_color, quit_button_rect)
        quit_text = font.render("Quit", True, pygame.Color("white"))
        quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
        screen.blit(quit_text, quit_text_rect)

        # Update the display
        pygame.display.update()
        
        # manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        #background.blit(desert, hexToPixel(75,0,0))
        #background.blit(desert, hexToPixel(75,0,1))

        # for q in range(5):
        #     for r in range(5):
        #         background.blit(desert, hexToPixel(75,q,r))
                
        


        
        # manager.draw_ui(window_surface)

        pygame.display.update()
pygame.quit()