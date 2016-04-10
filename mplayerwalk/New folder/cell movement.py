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

#Other varibals
BKG = BLACK
fps = 30
disWidth = 800
disHeight = 600
cellSize = 10
capt = 'Controlling'

#DIR
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'




def megsur(text,color):
    global setDisplay
    global fps
    smtxt = pygame.font.Font('freesansbold.tff',20)
    lgtxt = pygame.font.Font('freesansbold.tff',100)

    tittxtsur,tittxtrect = makeTextObjs(text,lgtext,textColor)
    tittxtrect.center = (int(disWidth/2),int(disHeight/2))
    setDisplay.blit(tittxtsur,tittxtrect)

    typtxt,tyttxtrect = makeTextObjs('Generic text',smtxt. WHITE)
    tyttxtrect.center = (int(disWidth/2),int(disHeight/2)+120)
    setDisplay.blit(tittxtsur,tyttxtrect)

















def runGame():
    startx = 3
    starty = 3
    coords = [{'x':startx,'y':starty}]
    dirc = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.quit()

            if event.type == KEYDOWN:

                if event.key == K_LEFT:
                    dirc = LEFT
                if event.type == K_RIGHT:
                    dirc = RIGHT
                if event.type == K_UP:
                    dirc = UP
                if event.type == K_DOWN:
                    dirc = DOWN
                
        if dirc == UP:
            newCell = {'x':coords[0] ['x'],'y':coords[0]['y']-1}
        elif dirc == DOWN:
            newCell = {'x':coords[0] ['x'],'y':coords[0]['y']+1}
        elif dirc == LEFT:
            newCell = {'x':coords[0] ['x']-1,'y':coords[0]['y']}
        elif dirc == RIGHT:
            newCell = {'x':coords[0] ['x']+1,'y':coords[0]['y']}

        del coords[-1]

        coords.insert(0, newCell)
        setDisplay.fill(BKG)
        drawCell(coords)
        pygame.display.update()
        fpsTime.tick(fps)
        
def drawCell(coords):
    global cellSize
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize,cellSize)
        pygame.draw.rect(setDisplay,WHITE,makeCell)


while True:
    global fpsTime,setDisplay
    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((disWidth,disHeight))
    pygame.display.set_caption(capt)
    megsur('message',WHITE)
    
    


