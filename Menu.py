import pygame

pygame.init()

#set up screen
screen_width = 800
screen_height = 600
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Pysettlers v1.0")

#aesthetics
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SELECTED_ITEM_COLOR = pygame.Color('red')
REGULAR_ITEM_COLOR = pygame.Color('white')
font = pygame.font.SysFont(None, 48)
ITEM_HEIGHT = font.get_linesize()

menu_items = ['New game', 'Options', 'Quit']
menu_top_margin = 200

for i, item in enumerate(menu_items):
    text = font.render(item, True, WHITE)
    text_rect = text.get_rect(center = (screen_width/2, menu_top_margin + i*50))
    screen.blit(text, text_rect)

selected_item = 0

#MAIN
running = True
while running:
    # Event handling
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item -= 1
                if selected_item < 0:
                    selected_item = 0
            elif event.key == pygame.K_DOWN:
                selected_item += 1
                if selected_item > 2:
                    selected_item = 2
            elif event.key == pygame.K_RETURN:
                if menu_items[selected_item] == 'Start Game':
                    # Start the game
                    print('Starting game...')
                elif menu_items[selected_item] == 'Options':
                    # Show the options menu
                    print('Showing options menu...')
                elif menu_items[selected_item] == 'Quit':
                    # Quit the game
                    running = False


        # Draw the menu items
    screen.fill((0, 0, 0))
    y = (screen_height - len(menu_items) * ITEM_HEIGHT) // 2
    for i, item in enumerate(menu_items):
        if i == selected_item:
            text_color = SELECTED_ITEM_COLOR
        else:
            text_color = REGULAR_ITEM_COLOR
        text_surface = font.render(item, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, y)
        screen.blit(text_surface, text_rect)
        y += ITEM_HEIGHT

    # Update the screen
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

