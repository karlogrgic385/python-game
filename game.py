from sys import exit
import pygame
import player, sprite, game_controls

# Global scope variables names' reservations
windowWidth = 768
windowHeight =  432
grassHeight = int(windowHeight * (2 / 3))
charInitX = 0
charInitY = grassHeight
gameFPS = 30 
charVel = 5
cloudVel = 1
gameWin = None
gameTimer = None

backgroundColour = (38, 146, 255)
charImg = pygame.image.load("assets/images/mainChar.bmp")
grassImg = pygame.image.load("assets/images/grass.bmp")

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

def movePlayer(pImg, x, y, d):
    pRect = pImg.get_rect()
    dx = pRect.x

charInitY = charInitY - charImg.get_size()[1]
initGame(windowHeight, windowWidth)

while True:
    gameWin.blit(charImg, (0, charInitY))

    for event in pygame.event.get():
        userCommand = game_controls.checkCommand(event)
        print(userCommand)
    
    if userCommand:
        movePlayer(charImg, charInitX, charInitY, charVel)

    #gameWin.blit() 
    # Update the display
    pygame.display.update()
    gameTimer.tick(gameFPS)
