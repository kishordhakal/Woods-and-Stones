import pygame
import numpy
import sys
from pygame import locals
#from frontpage import *

from random import sample 

pygame.init()

#SETTING UP HEIGHT AND WIDTH
WIDTH= 800
HEIGHT= 800

#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#title and icon

pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)

#backgroun image
background = pygame.image.load('bgpic.png')

#random choice ness
player = ['Player1', 'Player2']
x= sample(player,1)
if x[0]=="Player1":
        print("player 1 is stone")
else:
        print("player  2 is stone")





#main loop

while True:
        #loading background image 
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()



        pygame.display.flip()



