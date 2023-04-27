import pygame
import pygame_gui
from Game import *
from drawHex import hexToPixel




pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (150, 150, 255)
GREEN = ()

pygame.display.set_caption('Settlers')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT),'theme.json')

clock = pygame.time.Clock()




def main_menu():
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

    new_game = Game(4,mode)
    manager.clear_and_reset()
    is_running = True
      
    background.fill(BLACK)
    
    
    left_rect_width = SCREEN_WIDTH // 4 * 3
    left_rect_height = SCREEN_HEIGHT
    left_rect = pygame.Surface((left_rect_width, left_rect_height))
    left_rect.fill(BLUE)

    right_rect_width = SCREEN_WIDTH // 4
    right_rect_height = SCREEN_HEIGHT
    right_rect = pygame.Surface((right_rect_width, right_rect_height))
    right_rect.fill(WHITE)

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

    victory_points_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 6,250,150),text="Victory Points: " + str(new_game.current_player.victory_points),manager=manager)

    draw_board(new_game.board, left_rect)


    while is_running:
        time_delta = clock.tick(60)/1000.0
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
                    player_name_label.set_text("Player " + str(new_game.current_player.name))
                    victory_points_label.set_text("Victory Points: " + str(new_game.current_player.victory_points))
                    
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == build_road_button:
                    print("Build Road")
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == build_settlement_button:
                    print("Build Settlement")
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == upgrade_settlement_button:
                    print("Upgrade Settlement")
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == roll_dice_button:
                    print("Dice Roll")            
                
            manager.process_events(event)

        manager.update(time_delta)

        
        window_surface.blit(background, (0, 0))


        background.blit(left_rect, (0, 0))
        background.blit(right_rect, (left_rect_width, 0))

        manager.draw_ui(window_surface)

        pygame.display.update()


#import textures
def import_assets():
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


main_menu()