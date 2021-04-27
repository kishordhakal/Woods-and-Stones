#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 05:07:42 2021

@author: sawamurahinako
"""

import pygame
from pygame.locals import*
import pygame.freetype
import sys
from pygame import mixer

#initialize the pygame
pygame.init()


#title and icons
pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)

#game music
#background music
mixer.music.load('bgsound.mp3')
mixer.music.play(-1) #enabeling looping

#back button



def AboutPage():
    (w,h) = (800, 800) #画面サイズ
    pygame.init() #pygameの初期化
    pygame.display.set_mode((w,h), 0,32) #画面設定
    screen = pygame.display.get_surface()
    
    font1 = pygame.font.SysFont("comicsansms", 30)
    font2 = pygame.freetype.Font('C:\Windows\Fonts\FORTE.TTF', 80)
    
    
   # text1 = font2.render("About", True, (255, 255, 255))
    
    text2 = font1.render("Play occurs on a 3 by 3 grid of 9 empty squares. ", True, (255,255,255))
    
    text3 = font1.render("Two players alternate placing their items alternately  ", True, (255,255,255))
    
    text4 = font1.render("One player place stone, the other wood.", True, (255,255,255))
    
    text5 = font1.render("Repeat this three times.", True,(255,255,255) )
    
    text6 = font1.render("If one player places three of the same items in a", True,(255,255,255))
    
    text7= font1.render("row, that player wins.", True,(255,255,255))
    
    text8= font1.render("If there is no winner, the players can move their", True,(255,255,255))
     
    text9 = font1.render("stones or woods to the adjacent empty squares", True, (255, 255, 255))
    
    text10 = font1.render("alternately until the winner is decided.",True, (255, 255, 255) )
     
    


    #background image
    bg = pygame.image.load("bgpic.png").convert_alpha()
    rect_bg = bg.get_rect()

    while(1):
        pygame.display.update() #画面更新
        pygame.time.wait(100) #更新画面間隔
        screen.fill((0, 0, 0, 0)) #画面の背景色
        screen.blit(bg, rect_bg) #背景画像の描画
        
        pygame.draw.rect(screen,(0,80,0),Rect(30,100,745,150))
        
        pygame.draw.rect(screen,(0,80,0),Rect(30,270,745,150))
        
        pygame.draw.rect(screen,(0,80,0),Rect(30,440,745,150))


        pygame.draw.rect(screen,(191, 138, 23),Rect(0,0,800,80))
        
        font2.render_to(screen, (280,10), 'About', (255, 255, 255, 250))
        
        screen.blit(text2, (45,120))
        
        screen.blit(text3, (45,160))
        
        screen.blit(text4, (45,200))
        
        screen.blit(text5, (45,290))
        
        screen.blit(text6, (45,330))
        
        screen.blit(text7, (45,370))
        
        screen.blit(text８, (45,460))
         
        screen.blit(text９, (45,500))
        
        screen.blit(text10, (45,540))
        
     

     
        for event in pygame.event.get():
           
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ =="__main__":
        AboutPage()

