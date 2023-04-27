import pygame
import pygame_gui
from pygame_gui.elements.ui_window import UIWindow

class TradeWindow(UIWindow):
    def __init__(self,manager, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(
            rect=pygame.Rect(SCREEN_WIDTH // 4 * 3, 0, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2),
            manager=manager,
            window_display_title="Trade",
            visible=0)
        
        window_size = self.get_container().get_size()

        self.trade_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window_size[0] , window_size[1]), (100, 50)),
                                                text='Trade',tool_tip_text="Press To End Your Turn",manager=manager,parent_element = self,container=self)

    def on_close_window_button_pressed(self):
        self.hide()
    