import pygame
import pygame_gui
from pygame_gui.elements.ui_window import UIWindow
from Board import *

from TileResource import TileResource
from drawHex import hexToPixel, vertToPixel


pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

pygame.display.set_caption('Settlers')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT),'theme.json')




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = ()
GREEN = ()

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

#test board render

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


board = Grid(7)

board.defaultBoard()

#test player 




p1 = Player("Levi","RED")
p2 = Player("Player2","GREEN")
p3 = Player("Player3","BLUE")
p4 = Player("Player4","YELLOW")

players = [p1,p2,p3,p4]

current_player_index = 0
current_player = players[current_player_index]

#left side of ui

left_rect_width = SCREEN_WIDTH // 4 * 3
left_rect_height = SCREEN_HEIGHT
left_rect = pygame.Surface((left_rect_width, left_rect_height))
left_rect.fill((150, 150, 255))

#right side of ui
right_rect_width = SCREEN_WIDTH // 4
right_rect_height = SCREEN_HEIGHT
right_rect = pygame.Surface((right_rect_width, right_rect_height))
right_rect.fill(WHITE)

board_tiles_rect = pygame.Surface((left_rect_width, left_rect_height), pygame.SRCALPHA)
board_tiles_rect.fill((255,255,255,0))


def draw_board(skip, board, destination):
    
    for coord in board.tiles:
        if coord not in skip:
            pass
        if board.tiles[coord] != 'Water':
           destination.blit(textureToVal(board.tiles[coord].resource),hexToPixel(75,coord.q,coord.r, 0))
           pygame_gui.elements.UILabel(relative_rect=pygame.Rect(hexToPixel(75,coord.q,coord.r, 0)[0],hexToPixel(75,coord.q,coord.r, 0)[1],150,150),text=str(board.tiles[coord].returnNum()),object_id=pygame_gui.core.ObjectID(class_id='@rollNums'),manager=manager)
        
        elif coord not in skip and board.tiles[coord] == 'Water':
            destination.blit(water, hexToPixel(75,coord.q,coord.r, 0))


class VertButton:
    def __init__(self,screen, color, center, radius):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius
        self.is_active = True

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def is_clicked(self, mouse_pos):
        if self.is_active == True:
            distance = ((self.center[0] - mouse_pos[0]) ** 2 + (self.center[1] - mouse_pos[1]) ** 2) ** 0.5
            self.disable()
            return distance <= self.radius
    
    def disable(self):
        self.is_active = False
        


buttons = []

def print_verts(surface,list):
    x = 60
    y = 0
    for key in list:
        if key.s == 'N':
            button = VertButton(surface,'#FF0000',vertToPixel(75,key.q,key.r,x,y),10)
            buttons.append(button)
            #pygame.draw.circle(surface,'#FF0000',vertToPixel(75,key.q,key.r,x,y),10)

        if key.s =='S':
            pygame.draw.circle(surface,'#FFFFFF',vertToPixel(75,key.q,key.r,x,y + 75 * 2),10)

def print_buttons(surface,list):
    pass










build_road_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 300), (100, 50)),
                                            text='Build Road',
                                            manager=manager)

build_settlement_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 100, SCREEN_HEIGHT - 300), (100, 50)),
                                            text='Build Settlement',
                                            manager=manager)

upgrade_settlement_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 200, SCREEN_HEIGHT - 300), (100, 50)),
                                            text='Upgrade Settlement',
                                            manager=manager)


trade_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 200), (100, 50)),
                                            text='Trade',
                                            manager=manager)


end_turn_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 100, SCREEN_HEIGHT - 100), (100, 50)),
                                            text='End Turn',
                                            manager=manager)

roll_dice_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 100), (100, 50)),
                                            text='Roll Dice',
                                            manager=manager)



verts_rect = pygame.Surface((left_rect_width, left_rect_height), pygame.SRCALPHA)







empty_verts = []

def fill_empty_verts(dest):
    for coord in board.tiles.keys():
            if board.tiles[coord] != "Water":
                for key in corners(coord):
                    if board.vertices[key] == '':
                        if key in dest:
                            pass
                        else:
                            dest.append(key)

fill_empty_verts(empty_verts)

class TradeWindow(UIWindow):
    def __init__(self,manager):
        super().__init__(
            rect=pygame.Rect(SCREEN_WIDTH // 4 * 3, 0, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2),
            manager=manager,
            window_display_title="Trade",
            visible=0)
        
    def on_close_window_button_pressed(self):
        self.hide()

trade_window = TradeWindow(manager)



    
    



x  = SCREEN_WIDTH// 4 * 3
y = 0
yoffset = 50

print(current_player.name)

player_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y,150,150),text=str(current_player.name),manager=manager)
resources = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset - 25  ,150,150),text="Resources",manager=manager)

brick_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset,150,150),text="Brick: " + str(current_player.resources.get(TileResource.Brick)),manager=manager)
lumber_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 2,150,150),text="Lumber: " + str(current_player.resources.get(TileResource.Lumber)),manager=manager)
ore_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 3,150,150),text="Ore: " + str(current_player.resources.get(TileResource.Ore)),manager=manager)
grain_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 4,150,150),text="Grain: " + str(current_player.resources.get(TileResource.Grain)),manager=manager)
wool_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 5,150,150),text="Wool: " + str(current_player.resources.get(TileResource.Wool)),manager=manager)

victory_points_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(x,y + yoffset * 6,150,150),text="P1 Victory Points: " + str(current_player.victory_points),manager=manager)


clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    cursor = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == trade_button:
                trade_window.show()
                print('Trade')
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == end_turn_button:
                current_player_index = (current_player_index + 1) % len(players)
                current_player = players[current_player_index]
                player_name.set_text(current_player.name)
                victory_points_label.set_text(str(current_player.victory_points))
                print('End Turn')
                empty_verts.pop()
                
                
                
                
        

        manager.process_events(event)


    manager.update(time_delta)
    

    window_surface.fill(BLACK)

    window_surface.blit(background, (0, 0))
    
    left_rect.fill((150, 150, 255))

    draw_board(skip, board, left_rect)
    print_verts(left_rect,empty_verts)

    for button in buttons:
        button.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(cursor) == True:
                print("Clicked")
    
    

    # left_rect.blit(board_tiles_rect,(-100,50))
    # left_rect.blit(verts_rect,(-100,50))
    
    background.blit(left_rect, (0, 0))
    background.blit(right_rect, (left_rect_width, 0))

  
    manager.draw_ui(window_surface)

    
        
    pygame.display.flip()
    