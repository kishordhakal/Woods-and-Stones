import sys, pygame
pygame.init()

#title and icons
pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)


# Set size of the user screen
size = width, height = 800, 800

# Set colors for the screen background
background = (237, 196, 107)

# Create screen object to place checkerboard into
screen = pygame.display.set_mode(size)

# Load wood image for drawing in screen and get rectangle for click detection
wood = pygame.image.load("wood.png")
woodRect = wood.get_rect()

# Load stone image for drawing in screen and get rectangle for click detection
stone = pygame.image.load("stone.png")
stoneRect = stone.get_rect()

# Load checkerboard image for drawing in screen and get rectangle for click detection
board = pygame.image.load("board.png")
boardRect = board.get_rect()

# Load checkerboard image for drawing in screen and make an array of rectangles for click detection
# These detector rectangles are placed exactly where the board tiles are and can now be referenced through the array
tile = pygame.image.load("tile.png")
tileGrid = [tile.get_rect(x = 150, y = 150), tile.get_rect(x = 325, y = 150), tile.get_rect(x = 500, y = 150), # TOP ROW
            tile.get_rect(x = 150, y = 325), tile.get_rect(x = 325, y = 325), tile.get_rect(x = 500, y = 325), # MIDDLE ROW
            tile.get_rect(x = 150, y = 500), tile.get_rect(x = 325, y = 500), tile.get_rect(x = 500, y = 500)] # BOTTOM ROW

#colors for retry and quit
color = (255, 255, 255)
#colors for the different shades for the buttons
color_light = (77, 219, 181)
color_dark = (0, 180, 0)
BLACK=(0,0,0)
WHITE=(255,255,255)
#fonts and font size for retry and quit buttons
quitFont = pygame.font.SysFont("corbel", 60)
retryFont = pygame.font.SysFont("corbel", 55)
#the words for the buttons
quit = quitFont.render("Quit", True, color)
reset = retryFont.render("Reset", True, color)
menu= quitFont.render("Menu", True, color)

# Define method that creates player checkerboard and the screen it opens in
def playerboard():
    # Reference for whose turn it is
    playerTurn = 0

    # Draw blank checkerboard in screen
    draw()

    # Update screen
    pygame.display.flip()

    # Infinite loop that checks all input events for an exit command (hitting the red X button)
    while 1:
        # Check for any user event (mouse clicks, button presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #checks if mouse button was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #checks the location of the mouse click
                #mouse click for quit button then exits
                if width- 450 <= mouse[0] <= width-280 and height - 750 <= mouse[1] <= height - 700:
                    import frontpage
                    frontpage.main_menu()
                if width-200 <= mouse[0] <= width-80 and height-750 <= mouse[1] <= height-700:
                    sys.exit()
                # mouse click for retry button, but currently set to exit game until functionality
                # is added later on
                if width-700 <= mouse[0] <= width-580 and height-750 <= mouse[1] <= height-700:
                    draw()
                    pygame.display.flip()
                    playerTurn = 0
            # Check for mouse button release
            if event.type == pygame.MOUSEBUTTONUP:
                # For loop that goes through tileGrid array full of tile detector rectangles
                # collidepoint() checks the x, y position of mouse click and checks which board tile was clicked
                for i in range(0, 9):
                    if pygame.Rect.collidepoint(tileGrid[i], pygame.mouse.get_pos()):
                        # Modulus statement that flips between rock and stone picture placements
                        if playerTurn % 2 == 0 and playerTurn < 6:
                            # get_surface() takes a copy image of the current board
                            # blit() draws it on a currently undisplayed frame
                            screen.blit(pygame.display.get_surface(), (0, 0))
                            # Draw the stone picture over top of board copied above and centers image in a tile
                            screen.blit(stone, (tileGrid[i].x + 37, tileGrid[i].y + 37))
                            # Take undisplayed frame that's been drawn on and display it
                            pygame.display.flip()
                            # Increment player turn by 1 post-click
                            playerTurn += 1
                        elif playerTurn % 2 == 1 and playerTurn < 6:
                            # get_surface() takes a copy image of the current board
                            # blit() draws it on a currently undisplayed frame
                            screen.blit(pygame.display.get_surface(), (0, 0))
                            # Draw the wood picture over top of board copied above and centers image in a tile
                            screen.blit(wood, (tileGrid[i].x + 37, tileGrid[i].y + 37))
                            # Take undisplayed frame that's been drawn on and display it
                            pygame.display.flip()
                            # Increment player turn by 1 post-click
                            playerTurn += 1
                        else:
                            print("\nPlayer placement limit reached\nTime to shuffle the pieces\n")

        # gets the xy coordinates of the mouse
        mouse = pygame.mouse.get_pos()
        # creates the mouse hover over effect
        # if mouse is in these coordinates then creates the mouse over lighter shade
        if width - 200 <= mouse[0] <= width - 80 and height - 750 <= mouse[1] <= height - 700:
            pygame.draw.rect(screen, color_light, [width - 200, height - 750, 120, 55])
        else:
            # otherwise it always creates a darker shade for when the mouse is not over it
            pygame.draw.rect(screen, color_dark, [width - 200, height - 750, 120, 55])
        # creates the dark and light shades for the reset button
        if width - 700 <= mouse[0] <= width - 580 and height - 750 <= mouse[1] <= height - 700:
            pygame.draw.rect(screen, color_light, [width - 700, height - 750, 130, 55])
        else:
            pygame.draw.rect(screen, color_dark, [width - 700, height - 750, 130, 55])
        #creates the Dark and Light shdes for the menu button
        if width- 450 <= mouse[0] <= width-280 and height - 750 <= mouse[1] <= height - 700:
            pygame.draw.rect(screen, color_light, [width- 450, height-750,140,55])
        else:
            pygame.draw.rect(screen, color_dark, [width - 450, height -750, 140, 55])

        # displays the text and updates the display
        screen.blit(reset, (width - 700, height - 750))
        screen.blit(quit, (width - 200, height - 750))
        screen.blit(menu, (width - 450, height - 750 ))
        #SHADES FOR BUTTONS
        #RESET BUTTON
        pygame.draw.line(screen, WHITE, (100, 50), (230, 50), 3)  # top side
        pygame.draw.line(screen, WHITE, (100, 50), (100, 105), 3)  # left
        pygame.draw.line(screen, BLACK, (100, 105), (230, 105), 3)  # buttom
        pygame.draw.line(screen, BLACK, (230, 50), (230, 105), 3)  # right
        #MENU BUTTON
        pygame.draw.line(screen, WHITE, (350, 50), (490, 50), 3)  # top side
        pygame.draw.line(screen, WHITE, (350, 50), (350, 105), 3)  # left
        pygame.draw.line(screen, BLACK, (350, 105), (490, 105), 3)  # buttom
        pygame.draw.line(screen, BLACK, (490, 50), (490, 105), 3)  # right

        #QUIT BUTTON
        pygame.draw.line(screen, WHITE, (600, 50), (720, 50), 3)  # top side
        pygame.draw.line(screen, WHITE, (600, 50), (600, 105), 3)  # left
        pygame.draw.line(screen, BLACK, (600, 105), (720, 105), 3)  # buttom
        pygame.draw.line(screen, BLACK, (720, 50), (720, 105), 3)  # right


        pygame.display.update()

def draw():
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
# Run playerboard method
if __name__ == '__main__':
    playerboard()

