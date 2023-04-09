import pygame
import sys

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)

# Set up the Pygame window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hover Button")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the button circle and text
button_center = (400, 300)
button_radius = 25
button_text = font.render("Click Me!", True, BLACK)

# Load the image to display when the button is clicked
clicked_image = pygame.image.load("assets/Hex.png").convert_alpha()

# Define a custom sprite class
class HoverSprite(pygame.sprite.Sprite):
    def __init__(self, center, radius):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill(LIGHT_GRAY)
        self.rect = self.image.get_rect(center=center)
        self.clicked = False

    def update(self):
        if self.clicked:
            self.image = clicked_image
            self.rect = self.image.get_rect(center=self.rect.center)

# Create the button sprite group
button_group = pygame.sprite.Group()
button_sprite = HoverSprite(button_center, button_radius)
button_group.add(button_sprite)

# Define a dictionary to store game data
game_data = {
    "score": 0,
}

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if ((mouse_pos[0] - button_center[0])**2 + (mouse_pos[1] - button_center[1])**2) <= button_radius**2:
                button_sprite.clicked = True
                game_data["score"] += 1

        # Check for hover over the button
        mouse_pos = pygame.mouse.get_pos()
        if ((mouse_pos[0] - button_center[0])**2 + (mouse_pos[1] - button_center[1])**2) <= button_radius**2:
            button_color = LIGHT_GRAY
        else:
            button_color = GRAY

    # Draw the button and text
    pygame.draw.circle(screen, button_color, button_center, button_radius)
    screen.blit(button_text, (button_center[0] - button_radius + 10, button_center[1] - button_radius + 10))

    # Update the button sprite group
    button_group.update()
    button_group.draw(screen)

    # Draw the score
    score_text = font.render(f"Score: {game_data['score']}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()
