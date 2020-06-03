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
    logo = py.image.load("./Icons/snake64.png")
    py.display.set_icon(logo)
    py.display.set_caption("Snake")
    
    #starting snake Coord 
    startX = random.randint(3,squareX-5)
    startY = random.randint(1,squareX)
    sCoord = [{'x':startX,'y':startY},{'x':startX-1,'y':startY},{'x':startX-2,'y':startY}]

    #apple starting location
    apple = getRandom()

    #starting points
    global points
    points = 0
    py.font.init()

    #main loop
    direction = 'right'
    drawGrid()
    running = True
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
        sCoord = movement(direction,sCoord) #snake coordinates
        drawPoints(points)
        drawApple(apple,sCoord)
        drawSnake(sCoord)
        colide(sCoord)
        apple = point(apple,sCoord)
        #controlls if apple coordinates is in snake
        for coord in sCoord:
            if(apple == coord):
                apple = getRandom()
        py.display.update()
        if(points == 400):
            running = False

def drawGrid():
    for x in range(screenX):
        for y in range(screenY):
            rect = py.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            py.draw.rect(screen,(200, 200, 200),rect,1)

def drawSnake(snakeCoord):
    for coord in snakeCoord:    
        snakeRect = py.Rect(coord['x']*blockSize,coord['y']*blockSize,blockSize,blockSize)
        py.draw.rect(screen,(0,255,0),snakeRect)

def drawApple(pos,snakeCoord):
    x = pos['x']*blockSize
    y = pos['y']*blockSize
    appleImg = py.image.load("./Icons/apple25.png")
    screen.blit(appleImg,(x+2,y+1))
    #applerect = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    #py.draw.rect(screen,(255,0,0),applerect)

def drawPoints(points):
    myfont = py.font.SysFont('Comic Sans MS', 30)
    text = myfont.render('Points: ' + str(points), False, (255,255,0))
    fixBlock({'x':19,'y':0})
    screen.blit(text,(500,10))

#control points and apple spawn
def point(apple,snakeCoord):
    global points
    if(apple == snakeCoord[0]):
        points = points + 1
        snakeCoord.insert(0,apple)
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
    for i in range(len(snakeCoord)-1):
        if (head == snakeCoord[i+1]):
            py,quit()
   
#control movement
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
    py.draw.rect(screen,(0, 0, 0),rect)
    rect2 = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    py.draw.rect(screen,(200, 200, 200),rect2,1)

#get random Location
def getRandom():
    x = random.randint(0,squareX-1)
    y = random.randint(0,squareX-1)
    return {'x':x,'y':y} #returns the pair x y

#run main 
main()