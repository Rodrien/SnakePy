import pygame as py
import random
import sys

#Constants
FPS = 10
FPSCLOCK = py.time.Clock()
py.font.init()

screenX = 600
screenY = 600
blockSize = 30
squareX = int(600/blockSize) #how many squares in each line

#load logo and set window name and background
logo = py.image.load("./Icons/snake64.png")
py.display.set_icon(logo)
py.display.set_caption("Snake Game")
screen = py.display.set_mode((screenX,screenY))
background = py.image.load("./background.png")
screen.blit(background,(0,0))

def game():    
    screen.blit(background,(0,0))
    #starting snake Coord 
    startX = random.randint(3,squareX-5)
    startY = random.randint(1,squareX)
    sCoord = [{'x':startX,'y':startY},{'x':startX-1,'y':startY},{'x':startX-2,'y':startY}]

    #apple starting location
    apple = getRandom()

    #starting points
    global points
    points = 0

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
        screen.blit(background,(0,0))
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

def menu():
    myfont = py.font.SysFont('Comic Sans MS', 80)
    text = myfont.render('SnakePY!', False, (255,150,20))
    myfont2 = py.font.SysFont('Comic Sans MS', 50)
    text2 = myfont2.render('Enter to play', False, (255,250,20))
    
    #butt0 = py.Rect(20,0,300,150)
    #py.draw.rect(screen,(255,0,0),butt0)

    #main loop
    running = True
    while running: 
        FPSCLOCK.tick(FPS)
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_DOWN: #use up and down for selecting play/options
                    pass
                if event.key == py.K_UP:
                    pass
                if event.key == py.K_RETURN:
                    running = False
                    game()
        screen.blit(text,(50,30))
        screen.blit(text2,(50,85))

#colisions
def colide(snakeCoord):
    head = snakeCoord[0]
    x = head['x']
    y = head['y']
    if(x > 19 or y > 19 or x < 0 or y < 0):
        py.quit()
        exit()
    for i in range(len(snakeCoord)-1):
        if (head == snakeCoord[i+1]):
            py.quit()
            exit()

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
    #fixBlock({'x':19,'y':0})
    screen.blit(text,(500,10))

#control points and apple spawn
def point(apple,snakeCoord):
    global points
    if(apple == snakeCoord[0]):
        points = points + 1
        snakeCoord.insert(0,apple)
        #fixBlock(apple)
        apple = getRandom()
    return apple
   
#control movement
def movement(dir,snakeCoord):
    head = snakeCoord[0]
    x = head['x']
    y = head['y']
    tail = snakeCoord.pop()
    tailrect = py.Rect(tail['x']*blockSize,tail['y']*blockSize,blockSize,blockSize)
    py.draw.rect(screen,(0,0,0),tailrect)

    #reDraw the grid where the tail was
    #fixBlock(tail)

    if(dir == 'up'):
        snakeCoord.insert(0,{'x':x,'y':y-1})
    elif(dir == 'down'):
        snakeCoord.insert(0,{'x':x,'y':y+1})
    elif(dir == 'left'):
        snakeCoord.insert(0,{'x':x-1,'y':y})
    else: #right
        snakeCoord.insert(0,{'x':x+1,'y':y})
    return snakeCoord

#get random Location
def getRandom():
    x = random.randint(0,squareX-1)
    y = random.randint(0,squareX-1)
    return {'x':x,'y':y} #returns the pair x y

def fixBlock(pos):
    pass
    #rect = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    #py.draw.rect(screen,(0, 0, 0),rect)
    #rect2 = py.Rect(pos['x']*blockSize,pos['y']*blockSize,blockSize,blockSize)
    #py.draw.rect(screen,(200, 200, 200),rect2,1)

#start
menu()