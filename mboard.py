import sys, pygame
pygame.init()


# Tile class that drives wood/stone icon placement and tile detection
class Tile:
    # "image" is a pygame.Surface object given by pygame.image.load() when creating a Tile object
    # "tileoccupied" is a pygame.Rect (detector rectangle) object given by pygame.Surface.get_rect()
    # "x" and "y" are the coordinates for drawing detector rectangles
    def __init__(self, image, x, y, whatPlayer):
        self.tilepicture = image
        self.tileoccupied = None
        self.xcoord = x
        self.ycoord = y
        self.whatPlayer= whatPlayer

    # Method that places a detector rectangle after drawing a wood/stone icon, prevents overlapping icons
    def drawiconrect(self):
        # tilepicture.get_rect() gives a rectangle at x and y coordinates to "tileoccupied"
        self.tileoccupied = self.tilepicture.get_rect(x = self.xcoord, y = self.ycoord)
        # Actually place said detector rectangle on the game board using update() method and "tileoccupied"
        pygame.display.update(self.tileoccupied)

        # setter method to set the player placing the piece on the board
    def setWhatPlayer(self, whatPlayer):
            self.whatPlayer = whatPlayer

        # getter method to get what player placed what piece
    def getWhatPlayer(self):
            return self.whatPlayer

    # Method that removes the detector rectangle from "tileoccupied" and updates game board
    def eraseiconrect(self):
        self.tileoccupied = None
        pygame.display.update(None)

    # Method that returns "tilepicture" (a pygame.Rect object) for drawing on the game board
    def getrectangle(self):
        return self.tilepicture.get_rect(x = self.xcoord, y = self.ycoord)

    # Method that returns "tilepicture" (a pygame.Surface object), which holds the image of a game board tile
    def getimage(self):
        return self.tilepicture

    # Method that returns the x coordinate used to draw the "tileoccupied" rectangle
    def getxcoord(self):
        return self.xcoord

    # Method that returns the y coordinate used to draw the "tileoccupied" rectangle
    def getycoord(self):
        return self.ycoord

    # Method that returns "tileoccupied", which is either None or a pygame.Rect object
    def isoccupied(self):
        return self.tileoccupied

    def getWinner(self):

        # checks if player 1 has 3 in a row for vertical
        if tileGrid[0].getWhatPlayer() == 1 and tileGrid[3].getWhatPlayer() == 1 and tileGrid[6].getWhatPlayer() == 1:
            print("player one wins")
        elif tileGrid[1].getWhatPlayer() == 1 and tileGrid[4].getWhatPlayer() == 1 and tileGrid[7].getWhatPlayer() == 1:
            print("player one wins")
        elif tileGrid[2].getWhatPlayer() == 1 and tileGrid[5].getWhatPlayer() == 1 and tileGrid[8].getWhatPlayer() == 1:
            print("player one wins")

        # checks if player 1 has 3 in a row for horizontal
        elif tileGrid[0].getWhatPlayer() == 1 and tileGrid[1].getWhatPlayer() == 1 and tileGrid[2].getWhatPlayer() == 1:
            print("player one wins")
        elif tileGrid[3].getWhatPlayer() == 1 and tileGrid[4].getWhatPlayer() == 1 and tileGrid[5].getWhatPlayer() == 1:
            print("player one wins")
        elif tileGrid[6].getWhatPlayer() == 1 and tileGrid[7].getWhatPlayer() == 1 and tileGrid[8].getWhatPlayer() == 1:
            print("player one wins")

        # checks if player 1 has 3 in a row for the diagonal
        elif tileGrid[0].getWhatPlayer() == 1 and tileGrid[4].getWhatPlayer() == 1 and tileGrid[8].getWhatPlayer() == 1:
            print("player one wins")
        elif tileGrid[2].getWhatPlayer() == 1 and tileGrid[4].getWhatPlayer() == 1 and tileGrid[6].getWhatPlayer() == 1:
            print("player one wins")

        # checks if player 2 has 3 in a row for vertical
        if tileGrid[0].getWhatPlayer() == 2 and tileGrid[3].getWhatPlayer() == 2 and tileGrid[6].getWhatPlayer() == 2:
            print("player two wins")
        elif tileGrid[1].getWhatPlayer() == 2 and tileGrid[4].getWhatPlayer() == 2 and tileGrid[7].getWhatPlayer() == 2:
            print("player two wins")
        elif tileGrid[2].getWhatPlayer() == 2 and tileGrid[5].getWhatPlayer() == 2 and tileGrid[8].getWhatPlayer() == 2:
            print("player two wins")

        # checks if player 2 has 3 in a row for horizontal
        elif tileGrid[0].getWhatPlayer() == 2 and tileGrid[1].getWhatPlayer() == 2 and tileGrid[2].getWhatPlayer() == 2:
            print("player two wins")
        elif tileGrid[3].getWhatPlayer() == 2 and tileGrid[4].getWhatPlayer() == 2 and tileGrid[5].getWhatPlayer() == 2:
            print("player two wins")
        elif tileGrid[6].getWhatPlayer() == 2 and tileGrid[7].getWhatPlayer() == 2 and tileGrid[8].getWhatPlayer() == 2:
            print("player two wins")

        # checks if player 2 has 3 in a row for the diagonal
        elif tileGrid[0].getWhatPlayer() == 2 and tileGrid[4].getWhatPlayer() == 2 and tileGrid[8].getWhatPlayer() == 2:
            print("player two wins")
        elif tileGrid[2].getWhatPlayer() == 2 and tileGrid[4].getWhatPlayer() == 2 and tileGrid[6].getWhatPlayer() == 2:
            print("player two wins")

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

# Load checkerboard image for drawing in screen and make an array of Tile objects
# These Tile objects hold icons for the game board tiles and have methods for icon detection in the game loop
tilepicture = pygame.image.load("tile.png")
tileGrid = [Tile(tilepicture, 150, 150,0), Tile(tilepicture, 325, 150,0), Tile(tilepicture, 500, 150,0), # TOP ROW
            Tile(tilepicture, 150, 325,0), Tile(tilepicture, 325, 325,0), Tile(tilepicture, 500, 325,0), # MIDDLE ROW
            Tile(tilepicture, 150, 500,0), Tile(tilepicture, 325, 500,0), Tile(tilepicture, 500, 500,0)] # BOTTOM ROW
# Create sound file objects for placing wood and stone icons
stonesound = pygame.mixer.Sound("stonesound.mp3")
woodsound = pygame.mixer.Sound("woodsound.mp3")

#colors for retry and quit
color = (255, 255, 255)
#colors for the different shades for the buttons
color_light = (77, 219, 181)
color_dark = (0, 180, 0)
BLACK=(0,0,0)
WHITE=(255,255,255)
#colors for the different shades for the buttons
color_light = (100, 100, 100)
color_dark = (0, 180, 0)
#fonts and font size for retry and quit buttons
quitFont = pygame.font.SysFont("corbel", 60)
retryFont = pygame.font.SysFont("corbel", 55)
#the words for the buttons
quit = quitFont.render("Quit", True, color)
reset = retryFont.render("Reset", True, color)



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
                if width-200 <= mouse[0] <= width-80 and height-750 <= mouse[1] <= height-700:
                    sys.exit()
                # mouse click for retry button, but currently set to exit game until functionality
                # is added later on
                if width-700 <= mouse[0] <= width-580 and height-750 <= mouse[1] <= height-700:
                    # For loop clears the board of all wood/stone detector rectangles, giving a clean board after reset
                    for i in range(0, 9):
                        tileGrid[i].eraseiconrect()
                    draw()
                    pygame.display.flip()
                    playerTurn = 0
                    # Check for mouse button release
            if event.type == pygame.MOUSEBUTTONUP:
                # For loop that goes through tileGrid array full of game board tile detector rectangles
                for i in range(0, 9):
                    # collidepoint() checks the x, y position of mouse click
                    # getrectangle() gets a game board tile from the Tile object in tileGrid[i]
                    # The position of these two are compared and checks which board tile was clicked
                    if pygame.Rect.collidepoint(tileGrid[i].getrectangle(), pygame.mouse.get_pos()):
                        # isoccupied() checks current game board tile for a wood/stone detector rectangle
                        # If no detector (is None), tile has no wood/stone icon and can be clicked on
                        # Otherwise, tile has an icon in it and can't be clicked on anymore
                        if tileGrid[i].isoccupied() is None:
                            # Modulus statement that flips between wood and stone picture placements
                            if playerTurn % 2 == 0 and playerTurn < 6:
                                # get_surface() takes a copy image of the current board
                                # blit() draws it on a currently undisplayed frame
                                screen.blit(pygame.display.get_surface(), (0, 0))
                                # Draw the stone picture over top of board copied above and centers image in a tile
                                screen.blit(stone, (tileGrid[i].getxcoord() + 37, tileGrid[i].getycoord() + 37))
                                # Take undisplayed frame that's been drawn on and display it
                                pygame.display.flip()
                                # Play stone placement sound
                                stonesound.play()
                                # drawiconrect() fills the empty board tile with a wood/stone detector rectangle
                                # So now it can no longer be clicked on
                                tileGrid[i].drawiconrect()
                                # set the player detection for player 1 to check for three in a row
                                tileGrid[i].setWhatPlayer(1)
                                # Increment player turn by 1 post-click
                                playerTurn += 1
                                # checks if anyone has a three in a row yet
                                tileGrid[i].getWinner()
                            elif playerTurn % 2 == 1 and playerTurn < 6:
                                # get_surface() takes a copy image of the current board
                                # blit() draws it on a currently undisplayed frame
                                screen.blit(pygame.display.get_surface(), (0, 0))
                                # Draw the wood picture over top of board copied above and centers image in a tile
                                screen.blit(wood, (tileGrid[i].getxcoord() + 37, tileGrid[i].getycoord() + 37))
                                # Take undisplayed frame that's been drawn on and display it
                                pygame.display.flip()
                                # Play wood placement sound
                                woodsound.play()
                                # drawiconrect() fills the empty board tile with a wood/stone detector rectangle
                                # So now it can no longer be clicked on
                                tileGrid[i].drawiconrect()
                                # set the player detection for player 2 to check for three in a row
                                tileGrid[i].setWhatPlayer(2)
                                # Increment player turn by 1 post-click
                                playerTurn += 1
                                # checks if anyone has a three in a row yet
                                tileGrid[i].getWinner()
                            else:
                                print("Player placement limit reached, time to move the pieces")
                        else:
                            print("Tile is occupied, please press another tile")

        # gets the xy coordinates of the mouse
        mouse = pygame.mouse.get_pos()
        # creates the mouse hover over effect
        # if mouse is in these coordinates then creates the mouse over lighter shade
        if width - 200 <= mouse[0] <= width - 80 and height - 750 <= mouse[1] <= height - 700:
            pygame.draw.rect(screen, color_light, [width - 200, height - 750, 120, 55])
        else:
            # otherwise it always creates a darker shade for when the mouse is not over it
            pygame.draw.rect(screen, color_dark, [width - 200, height - 750, 120, 55])
        # creates the dark and light shades for the retry button
        if width - 700 <= mouse[0] <= width - 580 and height - 750 <= mouse[1] <= height - 700:
            pygame.draw.rect(screen, color_light, [width - 700, height - 750, 130, 55])
        else:
            pygame.draw.rect(screen, color_dark, [width - 700, height - 750, 130, 55])
        # RESET BUTTON
        pygame.draw.line(screen, WHITE, (100, 50), (230, 50), 3)  # top side
        pygame.draw.line(screen, WHITE, (100, 50), (100, 105), 3)  # left
        pygame.draw.line(screen, BLACK, (100, 105), (230, 105), 3)  # buttom
        pygame.draw.line(screen, BLACK, (230, 50), (230, 105), 3)  # right

        # QUIT BUTTON
        pygame.draw.line(screen, WHITE, (600, 50), (720, 50), 3)  # top side
        pygame.draw.line(screen, WHITE, (600, 50), (600, 105), 3)  # left
        pygame.draw.line(screen, BLACK, (600, 105), (720, 105), 3)  # buttom
        pygame.draw.line(screen, BLACK, (720, 50), (720, 105), 3)  # right

        # displays the text and updates the display
        screen.blit(reset, (width - 700, height - 750))
        screen.blit(quit, (width - 200, height - 750))

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
    screen.blit(tilepicture, (150, 150))
    screen.blit(tilepicture, (325, 150))
    screen.blit(tilepicture, (500, 150))
    # SECOND ROW
    screen.blit(tilepicture, (150, 325))
    screen.blit(tilepicture, (325, 325))
    screen.blit(tilepicture, (500, 325))
    # THIRD ROW
    screen.blit(tilepicture, (150, 500))
    screen.blit(tilepicture, (325, 500))
    screen.blit(tilepicture, (500, 500))
# Run playerboard method
if __name__ == '__main__':
    playerboard()
