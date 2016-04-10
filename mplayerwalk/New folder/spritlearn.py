import pygame , sys

from pygame.locals import *



pygame.init()


#color = (r,g,b,opat)
WHITE  =  (255,255,255,255)
BLACK  =  (0,0,0,255)
RED    =  (255,0,0,255)
GREEN  =  (0,255,0,255)
BLUE   =  (0,0,255,255)
CYAN   =  (0,255,255,255)
YELLOW =  (255,255,0,255)
PURPLE =   (255,0,255,255)


setDisplay = pygame.display.set_mode((400,400))
pygame.display.set_caption('Game')
setDisplay.fill(BLACK)


FPS = 90
img = pygame.image.load('e.png')
imgx = 10
imgy = 10
pixmov = 5
move = 'down'

fpsTime = pygame.time.Clock()

#GAME LOOP
while True:

########################################    Movement S
    if move == 'down':
      imgy += pixmov
      if imgy > 325:
          img = pygame.transform.rotate(img,90)
          move = 'right'
          
    elif move =='right':
        imgx +=pixmov
        if imgx > 325:
          img = pygame.transform.rotate(img,90)   #rotate(obj,degrees)counterclockwise
          move = 'up'

    elif move =='up':
        imgy -=pixmov
        if imgy < 0:
            img = pygame.transform.rotate(img,90)
            move = 'left'

    elif move =='left':
        imgx -=pixmov
        if imgx <0:
            img = pygame.transform.rotate(img,90)
            move = 'down'
            
########################################    Movement e
#============================================================
########################################    blit img S
            
    setDisplay.blit(img,(imgx,imgy))
    
########################################    blit img e
#============================================================
    
    for event in pygame.event.get():
##        print(event)  #Print to consel mouse pos & key press
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(FPS)
