import pygame
import newMain

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SELECTED_ITEM_COLOR = pygame.Color('red')
REGULAR_ITEM_COLOR = pygame.Color('white')
font = font = pygame.font.Font("assets\Courier New Regular.ttf", 48)
clock = pygame.time.Clock()
ITEM_HEIGHT = font.get_linesize()
MENU_ITEMS = ['Start Game', 'Options', 'Quit']

# Create the game screen and set the caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pysettlers v1.0")

def draw_menu_items(selected_item):
    """Draws the menu items on the screen"""
    screen.fill(BLACK)
    y = (SCREEN_HEIGHT - len(MENU_ITEMS) * ITEM_HEIGHT) // 2
    for i, item in enumerate(MENU_ITEMS):
        if i == selected_item:
            text_color = SELECTED_ITEM_COLOR
        else:
            text_color = REGULAR_ITEM_COLOR
        text_surface = font.render(item, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, y)
        screen.blit(text_surface, text_rect)
        y += ITEM_HEIGHT

def handle_events(selected_item):
    """Handles Pygame events, updating the selected menu item"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, selected_item
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item -= 1
                if selected_item < 0:
                    selected_item = 0
            elif event.key == pygame.K_DOWN:
                selected_item += 1
                if selected_item > len(MENU_ITEMS) - 1:
                    selected_item = len(MENU_ITEMS) - 1
            elif event.key == pygame.K_RETURN:
                if MENU_ITEMS[selected_item] == 'Start Game':
                    # Start the game
                    print('Starting game...')
                    newMain.run_game()
                elif MENU_ITEMS[selected_item] == 'Options':
                    # Show the options menu
                    print('Showing options menu...')
                elif MENU_ITEMS[selected_item] == 'Quit':
                    # Quit the game
                    return False, selected_item
    return True, selected_item

def run_menu():
    """Runs the menu loop"""
    selected_item = 0
    is_running = True
    while is_running:
        is_running, selected_item = handle_events(selected_item)
        draw_menu_items(selected_item)
        pygame.display.update()
        clock.tick(FPS)
        if is_running == False:
            pygame.quit()

    pygame.quit()

# Run the menu
if __name__ == "__main__":
    run_menu()