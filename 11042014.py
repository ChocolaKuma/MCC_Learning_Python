#==================================#
#Johnathan Hinebrook
#11-04-2014
#Class notes
#==================================#

########################################################################


#==================================#
#Imports
#==================================#
import time
import random
import sys
import pygame
from pygame.locals import *

#==================================#
#Classes
#==================================#







#==================================#
#Functions
#==================================#

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CBLUE = (100, 149, 237)


# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the text
text = basicFont.render('Hello world!', True, CBLUE, RED)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game while infadent loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#=================================================================================


##import pygame, sys, time
##from pygame.locals import *
##
### set up pygame
##pygame.init()
##
### set up the window
##WINDOWWIDTH = 400
##WINDOWHEIGHT = 400
##windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
##pygame.display.set_caption('Animation')
##
### set up direction variables
##DOWNLEFT = 1
##DOWNRIGHT = 3
##UPLEFT = 7
##UPRIGHT = 9
##
##MOVESPEED = 30
##
### set up the colors
##BLACK = (0, 0, 0)
##RED = (255, 0, 0)
##GREEN = (0, 255, 0)
##BLUE = (0, 0, 255)
##
### set up the block data structure
##b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
##b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
##b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
##
##
##
##b4 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
##b5 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
##b6 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
##blocks = [b1, b2, b3, b4,b5, b6]
##
### run the game loop
##while True:
##    # check for the QUIT event
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            sys.exit()
##
##    # draw the black background onto the surface
##    windowSurface.fill(BLACK)
##
##    for b in blocks:
##        # move the block data structure
##        if b['dir'] == DOWNLEFT:
##            b['rect'].left -= MOVESPEED
##            b['rect'].top += MOVESPEED
##        if b['dir'] == DOWNRIGHT:
##            b['rect'].left += MOVESPEED
##            b['rect'].top += MOVESPEED
##        if b['dir'] == UPLEFT:
##            b['rect'].left -= MOVESPEED
##            b['rect'].top -= MOVESPEED
##        if b['dir'] == UPRIGHT:
##            b['rect'].left += MOVESPEED
##            b['rect'].top -= MOVESPEED
##
##        # check if the block has move out of the window
##        if b['rect'].top < 0:
##            # block has moved past the top
##            if b['dir'] == UPLEFT:
##                b['dir'] = DOWNLEFT
##            if b['dir'] == UPRIGHT:
##                b['dir'] = DOWNRIGHT
##        if b['rect'].bottom > WINDOWHEIGHT:
##            # block has moved past the bottom
##            if b['dir'] == DOWNLEFT:
##                b['dir'] = UPLEFT
##            if b['dir'] == DOWNRIGHT:
##                b['dir'] = UPRIGHT
##        if b['rect'].left < 0:
##            # block has moved past the left side
##            if b['dir'] == DOWNLEFT:
##                b['dir'] = DOWNRIGHT
##            if b['dir'] == UPLEFT:
##                b['dir'] = UPRIGHT
##        if b['rect'].right > WINDOWWIDTH:
##            # block has moved past the right side
##            if b['dir'] == DOWNRIGHT:
##                b['dir'] = DOWNLEFT
##            if b['dir'] == UPRIGHT:
##                b['dir'] = UPLEFT
##
##        # draw the block onto the surface
##        pygame.draw.rect(windowSurface, b['color'], b['rect'])
##
##    # draw the window onto the screen
##    pygame.display.update()
##    time.sleep(0.02)



def main():
    #print('main')

    

    
#==================================#
    main()
#==================================#

########################################################################
