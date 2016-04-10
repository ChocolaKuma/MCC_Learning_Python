##Johnathan Hinebrook
##Week of 11-04-2014 Homework
##Python3.x
##Turn a box into a ball and make it bounce around on screen
##Due 11-08-2014 23:59:58

import pygame, sys, time
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Homework 11-04-2014 Johnathan Hinebrook')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 5

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CBLUE = (100, 149, 237)

# set up the block data structure
##b1 = {'rect':pygame.draw.circle(windowSurface, RED, (235,254),35,0), 'color':CBLUE, 'dir':UPLEFT}  #Know working draw

b1 = {'rect':pygame.draw.circle(windowSurface, CBLUE, (0,254),35,1), 'color':BLUE, 'dir':UPLEFT}



blocks = [b1]

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    for b in blocks:
        # move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        # check if the block has move out of the window
        if b['rect'].top < 0:
            # block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # block has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # block has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # draw the block onto the surface
##        pygame.draw.rect(windowSurface, b['color'], b['rect'])
##        pygame.draw.circle(windowSurface, b['color'], (235,254),35,1)
        pygame.draw.circle(windowSurface, b['color'], (235,254),10,1)

    # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)


##circle(Surface, color, pos, radius, width=0) -> Rect
