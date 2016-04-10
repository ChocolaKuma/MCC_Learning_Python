import pygame , sys

from pygame.locals import *



pygame.init()


#color = (r,g,b,opat)
WHITE =  (255,255,255,255)
BLACK =  (0,0,0,255)
RED   =  (255,0,0,255)
GREEN =  (0,255,0,255)
BLUE  =  (0,0,255,255)



setDisplay = pygame.display.set_mode((400,400))
pygame.display.set_caption('Game')

while True:
    for event in pygame.event.get():
##        print(event)  #Print to consel mouse pos & key press
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
