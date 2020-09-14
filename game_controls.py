import pygame as pg

def checkCommand(inComm):
    if inComm.type == pg.KEYDOWN:
        if inComm.key == pg.K_w or inComm.key == pg.K_SPACE:
            print("You pressed ", inComm.key)
            return "Jump"
        elif inComm.key == pg.K_a:
            print("You pressed ", inComm.key)
            return "moveLeft"
        elif inComm.key == pg.K_s:
            print("You pressed ", inComm.key)
            return "duckDown"
        elif inComm.key == pg.K_d:
            print("You pressed ", inComm.key)
            return "moveRight"
        elif inComm.key == pg.K_ESCAPE:
            print("You pressed ", inComm.key)
            return "pauseMenu"
        else:
            print("You pressed an unknown key: ", inComm.key)
    
    elif inComm.type == pg.KEYUP:
        return "keyReleased"

    elif inComm.type == pg.MOUSEMOTION:
        return "mousePointerMoved"

    elif inComm.type == pg.MOUSEBUTTONDOWN:
        if inComm.button == 1:
            print("You pressed the left mouse button")
        elif inComm.button == 2:
            print("You pressed the middle mouse button")
        elif inComm.button == 3:
            print("You pressed the right mouse button")
        elif inComm.button == 4:
            print("You scrolled forward")
        elif inComm.button == 5:
            print("You scrolled backwards")

    elif inComm.type == pg.MOUSEBUTTONUP:
        return "mouseButtonReleased"

    elif inComm.type == pg.ACTIVEEVENT:
        return "unknownActiveEvent"

    elif inComm.type == pg.USEREVENT:
        return "unknownUserEvent"

    elif inComm.type == pg.QUIT:
        from sys import exit
        exit()   

    else:
        return "unknownEvent"
