import pygame
from Board import Grid, Hex
from Player import Player
from TileResource import TileResource
from drawHex import hexToPixel

# Initialise Pygame
pygame.init()

# Set up the Pygame screen
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Split Screen Demo")

# Set up the font
FONT_SIZE = 20
font = pygame.font.SysFont(None, FONT_SIZE)

# Load textures
TEXTURE_PATHS = {
    TileResource.Brick: "assets/Brick.png",
    TileResource.Desert: "assets/Desert.png",
    TileResource.Grain: "assets/Grain.png",
    TileResource.Lumber: "assets/Lumber.png",
    TileResource.Ore: "assets/Ore.png",
    TileResource.Wool: "assets/Wool.png",
    "Water": "assets/Hex.png"
}
textures = {}
for resource, path in TEXTURE_PATHS.items():
    textures[resource] = pygame.image.load(path).convert_alpha()

def textureToVal(value):
    match value:
        case TileResource.Brick:
            return textures[TileResource.Brick]
        case TileResource.Desert:
            return textures[TileResource.Desert]
        case TileResource.Grain:
            return textures[TileResource.Grain]
        case TileResource.Lumber:
            return textures[TileResource.Lumber]
        case TileResource.Ore:
            return textures[TileResource.Ore]
        case TileResource.Wool:
            return textures[TileResource.Wool]
        
board = Grid(7)
board.defaultBoard()
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

# Set up players
player1 = Player("Levi","RED")
player2 = Player("Luke", "BLUE")
players = [player1, player2]
current_player = 0

# Set up the left rectangle
LEFT_RECT_WIDTH = SCREEN_WIDTH // 4 * 3
LEFT_RECT_HEIGHT = SCREEN_HEIGHT
left_rect = pygame.Surface((LEFT_RECT_WIDTH, LEFT_RECT_HEIGHT))
left_rect.fill((150, 150, 255))

# Set up the right rectangle
RIGHT_RECT_WIDTH = SCREEN_WIDTH // 4
RIGHT_RECT_HEIGHT = SCREEN_HEIGHT
right_rect = pygame.Surface((RIGHT_RECT_WIDTH, RIGHT_RECT_HEIGHT))
right_rect.fill((255, 255, 255))


# Initialize variables
resources = ["Brick", "Lumber", "Ore", "Grain", "Wool"]
board_tiles_rect = pygame.Surface((LEFT_RECT_WIDTH, LEFT_RECT_HEIGHT), pygame.SRCALPHA)
board_tiles_rect.fill((255,255,255,0))

# Define functions
def draw_board():
    for coord in board.tiles:
        if coord in skip:
            continue
        if board.tiles[coord] == "Water":
            board_tiles_rect.blit(textures["Water"], hexToPixel(75,coord.q,coord.r, 50))
        else:
            texture = textures[board.tiles[coord].resource]
            board_tiles_rect.blit(texture, hexToPixel(75,coord.q,coord.r, 50))

def render_resources(screen, font, resources, name, x, y):
    player_name = font.render(name, True, (0, 0, 0))
    screen.blit(player_name, (x, y - 25))

    for i, (key, value) in enumerate(resources.items()):
        key_str = str(key)
        key_surface = font.render(key_str, True, (0, 0, 0))
        screen.blit(key_surface, (x, y + (i * (key_surface.get_height() + 10))))
        value_surface = font.render(str(value), True, (0, 0, 0))
        screen.blit(value_surface, (x + 150, y + (i * (key_surface.get_height() + 10))))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player1.add_resource(TileResource.Sheep, 2)
                player2.add_resource(TileResource.Brick, 2)
        # Draw the screen
        screen.blit(left_rect, (0, 0))
        screen.blit(right_rect, (LEFT_RECT_WIDTH, 0))
        draw_board()
        left_rect.blit(board_tiles_rect, (-100, 0))
        render_resources(screen, font, player1.resources, player1.name, SCREEN_WIDTH - SCREEN_WIDTH / 8 - 100, SCREEN_HEIGHT - 800)
        render_resources(screen, font, player2.resources, player2.name, SCREEN_WIDTH - SCREEN_WIDTH / 8 - 100, SCREEN_HEIGHT - 600)

        pygame.display.update()

if __name__ == '__main__':
    main()