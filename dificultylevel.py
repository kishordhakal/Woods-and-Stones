import pygame, sys
from pygame import mixer
import pygame.freetype
from pygame.locals import*

import aiboard
import begineer
import intermediate
from aboutpage import *
from aiboard import *
from multiplayer import *
from begineer import *
from intermediate import *

#initialize the pygame
pygame.init()


#SETTING UP HEIGHT AND WIDTH
WIDTH= 800
HEIGHT= 800

#colors
ORANGE=(191,138, 23)
black= (0,0,0)
white= (255,255,255)
red= (255,0,0)
screen_width = 800
screen_height = 800
#initializing clicked
clicked = False
#font
font = pygame.freetype.Font('C:\Windows\Fonts\FORTE.TTF', 80)
font1 = pygame.font.SysFont('Constantia', 30)

textX=10
textY =10



#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#title and icon

pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)




#background Image
background=pygame.image.load('bgpic.png')

#background music
pygame.mixer.music.set_volume(0.1) #setting up the volume
mixer.music.load('bgsound.mp3')
mixer.music.play(-1) #enabeling looping


#Buttons
class button():
    button_col = (0, 150, 0)
    hover_col = (75, 200, 200)
    click_col = (50, 150, 255)
    text_col = black
    width = 300
    height = 80
    #init function to assign values to the object properties
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font1.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

single= button(200, 200, 'Beginner')
multi = button(200, 350, 'Intermediate')
about = button(200, 500, 'Advanced AI')
back= button(0,80,'Main menu')
quit = button(200, 650, 'Quit')




    #font for the button
smallfont = pygame.font.SysFont('Corbel', 35)



#MAIN LOOP
#function to avoid the circular import
def dificultymain():
 while True:

        #background image
        screen.blit(background,(0,0))
        # Global socre to fix the score bugs for begineer
        begineer.player_score = 0
        begineer.computer_score = 0
        # GLOBAL SCORE to fix the socre bugs for intermedite
        intermediate.player_score = 0
        intermediate.computer_score = 0

        #ai
        aiboard.player_score= 0
        aiboard.ai_score= 0



        for event in pygame.event.get():
            #pressed quit button
         if event.type == pygame.QUIT:
                sys.exit()
            #pressed begineer
        if back.draw_button():
            import frontpage
            frontpage.main_menu()
        if single.draw_button():
            begineerboard(False)
            #pressed intermediate
        if multi.draw_button():
            intermediateboard(False)
         #Advanced AI
        if about.draw_button():
            playerboard(False)
        #quit button
        if quit.draw_button():
            print('quit')
            sys.exit()





        pygame.draw.rect(screen, ORANGE, (0, 0, 800, 80))
        font.render_to(screen, (40, 10), 'WOODS and STONES', (255, 255, 255, 250))
        pygame.display.update()


if __name__ == '__main__':
    dificultymain()