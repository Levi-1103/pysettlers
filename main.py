import pygame
import pygame_gui
from Game import *
from drawHex import hexToPixel, vertToPixel

pygame.init()

#Constants

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (150, 150, 255)

pygame.display.set_caption('Settlers')

window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT),'theme.json')

button_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT),'theme.json')
clock = pygame.time.Clock()



def main_menu():
    '''Run game start menu'''
    is_running = True

    start_game = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Start Game',
                                             manager=manager)
    
    

    while is_running:
        background.fill(BLACK)
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_game:
                    mode_menu()
                    is_running = False

            manager.process_events(event)

        manager.update(time_delta)

        
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

def mode_menu():
    '''Run menu page for game modes'''
    manager.clear_and_reset()
    is_running = True

    default_board = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Default Board',
                                             manager=manager)
    
    random_board = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275 * 2), (100, 50)),
                                             text='Random Board',
                                             manager=manager)
    

    while is_running:
        background.fill(BLACK)
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == default_board:
                    game_loop("default")
                    is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == random_board:
                    game_loop("random")
                    is_running = False    

            manager.process_events(event)

        manager.update(time_delta)

        
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def game_loop(mode):
    '''Run main Screen'''

    new_game = Game(4,mode)
    manager.clear_and_reset()
    is_running = True
      
    background.fill(BLACK)
    
    #sets up left side of screen
    left_rect_width = SCREEN_WIDTH // 4 * 3
    left_rect_height = SCREEN_HEIGHT
    left_rect = pygame.Surface((left_rect_width, left_rect_height))
    left_rect.fill(BLUE)

    #sets up right side of screen

    right_rect_width = SCREEN_WIDTH // 4
    right_rect_height = SCREEN_HEIGHT
    right_rect = pygame.Surface((right_rect_width, right_rect_height))
    right_rect.fill(WHITE)

    verts_surface = pygame.Surface((left_rect_width, left_rect_height), pygame.SRCALPHA)
    verts_surface.fill((255,255,255,0))

    
    

    #set up buttons
    build_road_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 300), (100, 50)),
                                            text='Build Road', tool_tip_text="Press to Build a Road. It costs : 1 Brick + 1 Lumber",
                                            manager=manager)
    build_settlement_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 100, SCREEN_HEIGHT - 300), (100, 50)),
                                                text='Build Settlement', tool_tip_text="Press to Build a Settlement It costs: 1 Brick + 1 Lumber + 1 Grain + 1 Wool",
                                                manager=manager)
    upgrade_settlement_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 200, SCREEN_HEIGHT - 300), (100, 50)),
                                                text='Upgrade Settlement',
                                                manager=manager)
    trade_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 200), (100, 50)),
                                                text='Trade',tool_tip_text="Press To Bring Up Trade Menu",
                                                manager=manager)
    end_turn_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 100, SCREEN_HEIGHT - 100), (100, 50)),
                                                text='End Turn',tool_tip_text="Press To End Your Turn",
                                                manager=manager)
    roll_dice_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 100), (100, 50)),
                                                text='Roll Dice', tool_tip_text="Roll Dice To Get Resources",
                                                manager=manager)
    

    #set up labels
    x  = SCREEN_WIDTH// 4 * 3
    y = 0
    yoffset = 50    

    player_name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y,150,150),text="Player " + str(new_game.current_player.name),manager=manager)
    resources_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset - 25  ,150,150),text="Resources",manager=manager)

    brick_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset,150,150),text="Brick: " + str(new_game.current_player.resources.get(TileResource.Brick)),manager=manager)
    lumber_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 2,150,150),text="Lumber: " + str(new_game.current_player.resources.get(TileResource.Lumber)),manager=manager)
    ore_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 3,150,150),text="Ore: " + str(new_game.current_player.resources.get(TileResource.Ore)),manager=manager)
    grain_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 4,150,150),text="Grain: " + str(new_game.current_player.resources.get(TileResource.Grain)),manager=manager)
    wool_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 5,150,150),text="Wool: " + str(new_game.current_player.resources.get(TileResource.Wool)),manager=manager)

    victory_points_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 6,270,150),text="Victory Points: " + str(new_game.current_player.victory_points),manager=manager)

    draw_board(new_game.board, left_rect)

    empty_verts = []
    vert_buttons = []

    

    fill_empty_verts(empty_verts,new_game.board)

    while is_running:
        time_delta = clock.tick(60)/1000.0
        new_game.check_winner()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == trade_button:
                    #trade_window.show()
                    print('Trade')
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == end_turn_button:
                    new_game.end_turn()
                    verts_surface.fill((255,255,255,0))
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == build_road_button:
                    new_game.current_player.add_resource(TileResource.Brick, 1)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == build_settlement_button:
                    print_verts(verts_surface,empty_verts,vert_buttons)
                    print("Build Settlement")

                            
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == upgrade_settlement_button:
                    print("Upgrade Settlement")
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == roll_dice_button:
                    print("Dice Roll")
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for row in vert_buttons:
                    for button in row:
                        if event.ui_element == button:
                            #print(row[0])
                            try:
                                new_game.place_settlement(row[0],new_game.current_player)
                            except:
                                pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(100,100,100,100),html_message="Not Enough Resources!",manager=manager)
                            

                # if event.ui_element == vert_buttons[0][1]:
                #     print(vert_buttons[0][0])            

                
            button_manager.process_events(event)
            manager.process_events(event)

        button_manager.update(time_delta)
        manager.update(time_delta)

        
        window_surface.blit(background, (0, 0))


        background.blit(left_rect, (0, 0))
        background.blit(right_rect, (left_rect_width, 0))
        background.blit(verts_surface, (0, 0))


        update_labels(new_game, player_name_label, brick_label, lumber_label, ore_label, grain_label, wool_label, victory_points_label)

        
        manager.draw_ui(window_surface)
        button_manager.draw_ui(window_surface)
        pygame.display.update()

def update_labels(new_game, player_name_label, brick_label, lumber_label, ore_label, grain_label, wool_label, victory_points_label):
    player_name_label.set_text("Player " + str(new_game.current_player.name))
    victory_points_label.set_text("Victory Points: " + str(new_game.current_player.victory_points))
    brick_label.set_text("Brick: " + str(new_game.current_player.resources.get
        (TileResource.Brick)))
    lumber_label.set_text("Lumber: " + str(new_game.current_player.resources.get(TileResource.Lumber)))
    ore_label.set_text("Ore: " + str(new_game.current_player.resources.get(TileResource.Ore)))
    grain_label.set_text("Grain: " + str(new_game.current_player.resources.get(TileResource.Grain)))
    wool_label.set_text("Wool: " + str(new_game.current_player.resources.get(TileResource.Wool)))


def import_assets():
    '''Import Game Assets'''
    desert = pygame.image.load("assets\Desert.png").convert_alpha() #120x140
    brick = pygame.image.load("assets\Brick.png").convert_alpha()
    grain = pygame.image.load("assets\Grain.png").convert_alpha()
    lumber = pygame.image.load("assets\Lumber.png").convert_alpha()
    ore = pygame.image.load("assets\Ore.png").convert_alpha()
    wool = pygame.image.load("assets\Wool.png").convert_alpha()
    water = pygame.image.load("assets\Hex.png").convert_alpha()
    return desert,brick,grain,lumber,ore,wool,water

desert, brick, grain, lumber, ore, wool, water = import_assets()

def textureToVal(value):
    '''Converts resources for a tile into a texture'''
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

def draw_board(board, destination):
    '''
    Draws draws board tiles and tile numbers onto screen

    '''

    #Empty tiles from grid that need to be skipped to have the hexagonal catan board shape
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
           destination.blit(textureToVal(board.tiles[coord].resource),hexToPixel(75,coord.q,coord.r, 0))
           pygame_gui.elements.UILabel(relative_rect=pygame.Rect(hexToPixel(75,coord.q,coord.r, 0)[0],hexToPixel(75,coord.q,coord.r, 0)[1],150,150),text=str(board.tiles[coord].returnNum()),object_id=pygame_gui.core.ObjectID(class_id='@rollNums'),manager=manager)
        
        elif coord not in skip and board.tiles[coord] == 'Water':
            destination.blit(water, hexToPixel(75,coord.q,coord.r, 0))



def fill_empty_verts(dest,board):
    for coord in board.tiles.keys():
            if board.tiles[coord] != "Water":
                for key in corners(coord):
                    if board.vertices[key] == '':
                        if key in dest:
                            pass
                        else:
                            dest.append(key)



def print_verts(surface,list,buttons):    
    x = 60
    y = 0
    for key in list:
        if key.s == 'N':
            #button = VertButton(surface,'#FF0000',vertToPixel(75,key.q,key.r,x,y),10)
            #buttons.append(button)
            buttons.append((key,pygame_gui.elements.UIButton(relative_rect=pygame.Rect((vertToPixel(75,key.q,key.r,50,-10)), (25, 25)),
                                            text='',object_id=pygame_gui.core.ObjectID(class_id='@vertButtons'),
                                            manager=manager)))
            #pygame.draw.circle(surface,'#FF0000',vertToPixel(75,key.q,key.r,x,y),10)

        if key.s =='S':
            #pygame.draw.circle(surface,'#FFFFFF',vertToPixel(75,key.q,key.r,x,y + 75 * 2),10)
            buttons.append((key,pygame_gui.elements.UIButton(relative_rect=pygame.Rect((vertToPixel(75,key.q,key.r,50,-10 + 75 * 2)), (25, 25)),
                                            text='',object_id=pygame_gui.core.ObjectID(class_id='@vertButtons'),
                                            manager=manager)))
            # pygame_gui.elements.UIButton(relative_rect=pygame.Rect((vertToPixel(75,key.q,key.r,50,-10 + 75 * 2)), (25, 25)),
            #                                 text='',object_id=pygame_gui.core.ObjectID(class_id='@vertButtons'),
            #                                 manager=manager)

main_menu()