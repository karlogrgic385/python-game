from sys import exit
import pygame

# Global scope variables names' reservations
windowHeight = 768
windowWidth =  432
gameFPS = 30 
charVel = 5
quitGame = False
gameWin = None
gameTimer = None

backgroundColour = (225, 225, 225)
charImg = pygame.image.load( "assets/images/mainChar.bmp" )

def initGame(wHei, wWid):
    global gameTimer
    global gameWin

    pygame.init()
    gameTimer = pygame.time.Clock()    
    gameWin = pygame.display.set_mode( (wHei, wWid) )  
    pygame.display.set_caption("Python Runner by KG")

initGame(windowHeight, windowWidth)

while quitGame != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            break

        keys = pygame.key.get_pressed()

        # Update the display
        pygame.display.update()
        gameTimer.tick( gameFPS )

if quitGame == True:
    exit()