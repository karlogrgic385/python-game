from sys import exit
import pygame
import player, sprite, game_controls

# Global scope variables names' reservations
windowWidth = 768
windowHeight =  432
grassHeight = int(windowHeight * (2 / 3))
gameFPS = 30 
charVel = 5
cloudVel = 1
gameWin = None
gameTimer = None

backgroundColour = (38, 146, 255)
charImg = pygame.image.load("assets/images/mainChar.bmp")
grassImg = pygame.image.load("assets/images/grass.bmp")
charSize = charImg.get_size()
charInitX = 0
charInitY = grassHeight - charSize[1]
dx = charInitX
dy = charInitY

def initGame(wHei, wWid):
    global gameTimer
    global gameWin
    pygame.init()
    gameTimer = pygame.time.Clock()    
    gameWin = pygame.display.set_mode((wWid, wHei)) 
    pygame.display.set_caption("Python Runner")
    gameWin.fill(backgroundColour)
    for x in range(0, windowWidth, 20):
        for y in range(grassHeight, windowHeight, 25):
            gameWin.blit(grassImg, (x, y))

def movePlayer(pImg, pComm, x, y, d):
    pRect = pImg.get_rect()
    currX = pRect.x
    currY = pRect.y
    dx = currX
    dy = currY

    if pComm == "moveRight" and currX <= (windowWidth-0.5*charSize[0]):
        dx = currX + d
    elif pComm == "moveLeft" and currX >= 0.5*charSize[0]:
        dx = currX - d
    elif pComm == "Jump" and currY <= (windowWidth-0.5*charSize[1]):
        dy = currY + d
    elif pComm == "duckDown" and currY >= charInitY:
        dy = currY - d 

initGame(windowHeight, windowWidth)
while True:
    for event in pygame.event.get():
        userCommand = game_controls.checkCommand(event)
        if userCommand:
            movePlayer(charImg, userCommand, charInitX, charInitY, charVel)
    
    #gameWin.blit() 
    # Update the display
    gameWin.blit(charImg, (dx, dy))
    pygame.display.update()
    gameTimer.tick(gameFPS)
