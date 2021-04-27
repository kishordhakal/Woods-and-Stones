import sys, pygame
pygame.init()

#title and icons
pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)


# Set size of the user screen
size = width, height = 800, 800

# Set colors for the screen background
background = (85,63,35)

# Load checkerboard/tile images and get rectangles for drawing in screen
board = pygame.image.load("board.png")
boardRect = board.get_rect()
tile = pygame.image.load("tile.png")
tileRect = tile.get_rect()

# Define method that creates player checkerboard and the screen it opens in
def playerboard():
    # Create screen object
    screen = pygame.display.set_mode(size)

    # Fill screen with black background
    screen.fill(background)

    # Fill background with checkerboard background, keeping board centered in screen
    # Checkboard is 550px by 550px and screen is 800px, giving 125px of room on all sides of the board ((800 - 550) / 2)
    screen.blit(board, (125, 125))

    # Fill checkboard background with board tiles
    # Each tile is 150px by 150px with a 25px gap between them, so each new tile is placed 175px from the previous one
    # FIRST ROW
    screen.blit(tile, (150, 150))
    screen.blit(tile, (325, 150))
    screen.blit(tile, (500, 150))
    # SECOND ROW
    screen.blit(tile, (150, 325))
    screen.blit(tile, (325, 325))
    screen.blit(tile, (500, 325))
    # THIRD ROW
    screen.blit(tile, (150, 500))
    screen.blit(tile, (325, 500))
    screen.blit(tile, (500, 500))

    # Update screen
    pygame.display.update()

    # Infinite loop that checks all input events for an exit command (hitting the red X button)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# Run playerboard method
if __name__ == '__main__':
    playerboard()
