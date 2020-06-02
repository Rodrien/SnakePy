import pygame as py
import random
import sys

#Constants
FPS = 15
screenX = 600
screenY = 600
blockSize = 30
squareX = int(600/blockSize) #how many squares in each line
screen = py.display.set_mode((screenX,screenY))

def main():
    #load logo and set window name
    #logo = py.image.load()
    #py.display.set_icon(logo)
    py.display.set_caption("Snake")
    
    #starting snake Coord
    startX = random.randint(3,squareX-5)
    startY = random.randint(1,squareX)
    sCoord = [{'x':startX,'y':startY},{'x':startX-1,'y':startY},{'x':startX-2,'y':startY}]

    #apple starting location
    appleStart = getRandom()

    #main loop
    running = True
    direction = 'right'
    drawApple(appleStart)
    while running:
        drawGrid()
        drawSnake(sCoord)
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_DOWN:
                    direction = 'down'
                    print("key down")
                if event.key == py.K_UP:
                    direction = 'up'
                    print("key up")
                if event.key == py.K_LEFT:
                    direction = 'left'
                    print("key left")
                if event.key == py.K_RIGHT:
                    direction = 'right'
                    print("key right")
        movement(direction,sCoord)
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

#colisions
def colide():
    pass

#movement
def movement(dir,snakeCoord):
    pass

#get random Location
def getRandom():
    x = random.randint(0,squareX)
    y = random.randint(0,squareX)
    return {'x':x,'y':y} #returns de pair x y

#run main 
main()




'''usfuell stuff
http://inventwithpython.com/pygame/chapter6.html
FPSCLOCK = pygame.time.Clock()
global FPSCLOCK, DISPLAYSURF, BASICFONT'''
