import pygame
import numpy
import sys
from pygame import locals
import mboard


from random import sample 

pygame.init()

#SETTING UP HEIGHT AND WIDTH
WIDTH= 800
HEIGHT= 800

# font for text
font1 = pygame.font.SysFont("comicsansms", 80)
font2 = pygame.font.SysFont("comicsansms",35)
font3 = pygame.font.SysFont("comicsansms",35)
#Colors
BLACK= (0,0,0)
BLUE= (66,209,245)
WHITE= (255,255,255)
Color =(52, 235, 172)

#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#title and icon

pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)

#backgroun image
background = pygame.image.load('bgpic.png')

#ok Button
# button
text_ok_button = font1.render("OK", True, (255, 255, 255))
ok_button = pygame.Rect(270, 650, 250, 100)


#loading the wood and stone pictures
wood= pygame.image.load("wood.png")
stone=pygame.image.load("stone.png")

#random choice ness
player = ['Player1', 'Player2']
x= sample(player,1)
if x[0]=="Player1":
        print("Player 1 is Stone")
        playerturn="Player 1 is Stone"
        playerturn2= "Player 2 is Wood"
        label1 = font2.render(playerturn, True, (255, 255, 255))
        label2 = font2.render(playerturn2, True, (255, 255, 255))
        
else:
        print("Player 2 is stone")
        playerturn="Player 1 is Wood"
        playerturn2= "Player 2 is Stone"
        label1 = font2.render(playerturn2, True, (255, 255, 255))
        label2 = font2.render(playerturn, True, (255, 255, 255))

#lABELS
label3 = font3.render("Stone always goes first", True, (255, 255, 255))






#main loop
def multiplayer():
  while True:
        pygame.display.update()
        #loading background image 
        screen.blit(background,(0,0))
        #draw rectangles
        pygame.draw.rect(screen, BLUE, (20, 40, 350, 350))
        pygame.draw.rect(screen, BLUE, (420, 40, 350, 350))

        # Rectangle for "Stones always go first"
        pygame.draw.rect(screen, Color, (20, 400, 750, 100))

        # button
        pygame.draw.rect(screen, (0, 150, 0), ok_button)
        screen.blit(text_ok_button, (315, 635))

        #BUTTON SHADING
        pygame.draw.line(screen, WHITE, (269, 649), (519, 649), 3)  # top side
        pygame.draw.line(screen, WHITE, (269, 649), (269, 749), 3)  # left
        pygame.draw.line(screen, BLACK, (269, 749), (519, 749), 3)  # buttom
        pygame.draw.line(screen, BLACK, (519, 649), (519, 749), 3)  # right

        #Lables
        screen.blit(label1, (50, 200))
        screen.blit(label2, (450, 200))
        screen.blit(label3, (150, 400))



        #Pictures on both rectangle.
        screen.blit(stone, (140,60))
        screen.blit(wood, (560, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()
            #checking if button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.collidepoint(event.pos):
                    print("okay button was pressed")
                    mboard.playerboard(False)





                pygame.display.flip()



