import pygame
import pygame_gui

pygame.init()

width = 1280
height = 720

pygame.display.set_caption('The Settlers')
window_surface = pygame.display.set_mode((width, height))

background = pygame.Surface((width, height))
background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((width, height))

new_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 480), (100, 50)), text='New Game', manager=manager)

settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 480), (100, 50)), text='Settings', manager=manager)

quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((950, 480), (100, 50)), text='Quit', manager=manager)

quit_x = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 100), (100, 50)), text='X', manager=manager)

#minimize_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 50)), text='_', manager=manager)

#credits_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 50)), text='Credits', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
