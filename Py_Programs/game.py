import pygame,sys, time
from pygame.locals import *
from time import *

def game():
    pygame.init()
    screen = pygame.display.set_mode((500, 400)) 
    pygame.display.set_caption("IDK What i just did!?") 
    B = (0,0,0) 
    R = (250,0,0)
    info = pygame.display.Info()

    sw = info.current_w 
    sh = info.current_h
    y = 0 
    x=0
    direction = 1 
    direction1=1
    while True: 
        screen.fill(B) 
        pygame.draw.circle(screen, R , (x,y), 13, 0)
        sleep(.006)
        x+=direction1
        y += direction  
        if y >= sh : 
            direction = -1 
        elif y <= 0:
            direction = 1 
        if x >= sh : 
            direction1 = -1 
        elif x <= 0:
            direction1 = 1 
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] : 
            direction = -5
        elif keys[pygame.K_DOWN] : 
            direction = 5
        elif keys[pygame.K_LEFT] : 
            direction1 = -5
        elif keys[pygame.K_RIGHT] : 
            direction1 = 5
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 
game()