import pygame

# Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 20

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Settlers of Catan")

# Create a font object for displaying text
font = pygame.font.SysFont(None, FONT_SIZE)

# Define player colors
PLAYER_COLORS = {
    1: (255, 0, 0),   # Red
    2: (0, 255, 0),   # Green
    3: (0, 0, 255),   # Blue
    4: (255, 255, 0), # Yellow
}

# Define the players
players = [
    {"name": "Player 1", "color": PLAYER_COLORS[1]},
    {"name": "Player 2", "color": PLAYER_COLORS[2]},
    {"name": "Player 3", "color": PLAYER_COLORS[3]},
    {"name": "Player 4", "color": PLAYER_COLORS[4]},
]

# Define the current player index and set it to the first player
current_player_index = 0
current_player = players[current_player_index]

# Define a list of actions that a player can take on their turn
actions = ["Build a road", "Build a settlement", "End turn"]

# Define a function for drawing the game screen
def draw_game():
    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)
    
    # Draw the player's name and color
    player_text = font.render(current_player["name"], True, FONT_COLOR)
    player_rect = player_text.get_rect(center=(WINDOW_WIDTH/2, 20))
    screen.blit(player_text, player_rect)
    
    player_color_rect = pygame.Rect(20, 20, 20, 20)
    player_color_rect.centerx = player_rect.left - 10
    pygame.draw.rect(screen, current_player["color"], player_color_rect)
    
    # Draw the available actions
    for i, action in enumerate(actions):
        action_text = font.render(action, True, FONT_COLOR)
        action_rect = action_text.get_rect(center=(WINDOW_WIDTH/2, 100 + i*50))
        screen.blit(action_text, action_rect)
    
    # Update the display
    pygame.display.flip()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i, action in enumerate(actions):
                action_text = font.render(action, True, FONT_COLOR)
                action_rect = action_text.get_rect(center=(WINDOW_WIDTH/2, 100 + i*50))
                if action_rect.collidepoint(pos):
                    if action == "End turn":
                        # End the current player's turn and move on to the next player
                        current_player_index = (current_player_index + 1) % len(players)
                        current_player = players[current_player_index]
                    else:
                        # Handle the selected action
                        pass

    # Update the game screen
    draw_game()

# Quit Pygame
pygame.quit()
