import pygame as p
import math as m
import random
from pgzhelper import*


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

screenWidth = 640
screenHeight = 480


def learnGame():
 
    p.init()
    size = (screenWidth, screenHeight)
    screen = p.display.set_mode(size)
    p.display.set_caption("Alyssa's Flappy Bird")
    running = True 
    clock = p.time.Clock()
    
     
    # -------- Main Program Loop -----------
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        
        key = p.key.get_pressed()

        if (key[p.K_ESCAPE] == True):
            running = False
        if (key[p.K_UP] == True):
            pass
        if (key[p.K_DOWN] == True):
            pass
        if (key[p.K_LEFT] == True):
            pass
        if (key[p.K_RIGHT] == True):
            pass
        if (key[p.K_SPACE] == True):
            pass
   
  
          
        background_image = p.image.load('images\\background.png')
        screen.fill(BLACK)
        # p.image.load(background_image)
        # screen.blit( background_image, ( screenWidth,screenHeight ) )
        # screen.fill(background_image)
        screen.blit( background_image, ( 0,0 ) )
        # --- Drawing code should go here
     
            
        p.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    p.quit()
    
    return


learnGame()