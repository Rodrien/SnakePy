import pygame as py
import random
import sys

#Constants
FPS = 10
FPSCLOCK = py.time.Clock()
screenX = 600
screenY = 600
blockSize = 30
squareX = int(600/blockSize) #how many squares in each line
screen = py.display.set_mode((screenX,screenY))

def main():
    #load logo and set window name
    logo = py.image.load("./Logos/snake64.png")
    py.display.set_icon(logo)
    py.display.set_caption("Snake")
    
    #starting snake Coord
    startX = random.randint(3,squareX-5)
    startY = random.randint(1,squareX)
    sCoord = [{'x':startX,'y':startY},{'x':startX-1,'y':startY},{'x':startX-2,'y':startY}]

    #apple starting location
    apple = getRandom()

    #main loop
    running = True
    direction = 'right'
    drawGrid()
    while running: 
        FPSCLOCK.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_DOWN:
                    direction = 'down'
                if event.key == py.K_UP:
                    direction = 'up'
                if event.key == py.K_LEFT:
                    direction = 'left'
                if event.key == py.K_RIGHT:
                    direction = 'right'
        sCoord = movement(direction,sCoord)
        apple = point(apple,sCoord)
        drawApple(apple)
        drawSnake(sCoord)
        colide(sCoord)
        py.display.update()

#draw grid
def drawGrid():
    for x in range(screenX):
        for y in range(screenY):
            rect = py.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            py.draw.rect(screen,(200, 200, 200),rect,1)

#draw snake
def drawSnake(snakeCoord):
    for coord in snakeCoord:    
        snakeRect = py.Rect(coord['x']*blockSize,coord['y']*blockSize,blockSize,blockSize)
        py.draw.rect(screen,(0,255,0),snakeRect)

#draw apple
def drawApple(pos): 
    applerect = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    py.draw.rect(screen,(255,0,0),applerect)

#point
def point(apple,snakeCoord):
    if(apple == snakeCoord[0]):
        fixBlock(apple)
        apple = getRandom()

    return apple

#colisions
def colide(snakeCoord):
    head = snakeCoord[0]
    x = head['x']
    y = head['y']
    if(x > 19 or y > 19 or x < 0 or y < 0):
        py.quit()

#movement
def movement(dir,snakeCoord):
    head = snakeCoord[0]
    x = head['x']
    y = head['y']
    tail = snakeCoord.pop()
    tailrect = py.Rect(tail['x']*blockSize,tail['y']*blockSize,blockSize,blockSize)
    py.draw.rect(screen,(0,0,0),tailrect)

    #reDraw the grid where the tail was
    fixBlock(tail)

    if(dir == 'up'):
        snakeCoord.insert(0,{'x':x,'y':y-1})
    elif(dir == 'down'):
        snakeCoord.insert(0,{'x':x,'y':y+1})
    elif(dir == 'left'):
        snakeCoord.insert(0,{'x':x-1,'y':y})
    else: #right
        snakeCoord.insert(0,{'x':x+1,'y':y})
    return snakeCoord

def fixBlock(pos):
    rect = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    py.draw.rect(screen,(200, 200, 200),rect,1)

#get random Location
def getRandom():
    x = random.randint(0,squareX-1)
    y = random.randint(0,squareX-1)
    return {'x':x,'y':y} #returns de pair x y

#run main 
main()


#TO-DO
#Apple cant spawn in the snake
#Borders
#change apple location when the snake eats it

'''usfuell stuff
http://inventwithpython.com/pygame/chapter6.html
FPSCLOCK = pygame.time.Clock()
global FPSCLOCK, DISPLAYSURF, BASICFONT'''
