import pygame
import pygame_gui
from pygame_gui.elements.ui_window import UIWindow


pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

pygame.display.set_caption('Settlers')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT),'theme.json')

left_rect_width = SCREEN_WIDTH // 4 * 3
left_rect_height = SCREEN_HEIGHT
left_rect = pygame.Surface((left_rect_width, left_rect_height))
left_rect.fill((150, 150, 255))

right_rect_width = SCREEN_WIDTH // 4
right_rect_height = SCREEN_HEIGHT
right_rect = pygame.Surface((right_rect_width, right_rect_height))
right_rect.fill((255, 255, 255))



end_turn_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT - 100), (100, 50)),
                                            text='End Turn',
                                            manager=manager)

roll_dice_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3 + 100, SCREEN_HEIGHT - 100), (100, 50)),
                                            text='Roll Dice',
                                            manager=manager)

trade_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 4 * 3, 200), (100, 50)),
                                            text='Trade',
                                            manager=manager)

player_name_label = pygame_gui.elements.UILabel(pygame.Rect((SCREEN_WIDTH // 4 * 3,0), (100,50)),
                                                        "Player Name",
                                                        manager=manager)

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






clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == trade_button:
                trade_window.show()
                print('Trade')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    background.blit(left_rect, (0, 0))
    background.blit(right_rect, (left_rect_width, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()