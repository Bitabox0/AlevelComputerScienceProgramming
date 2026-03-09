import pygame as pg
import math
import random

#>--------------------------------------------------------------<#

class Car(pg.sprite.Sprite):
    def __init__(self, width, height, colour, pos):
        super().__init__()
        self.width = width
        self.height = height
        self.colour = colour
        self.pos = pos
        self.centre = pg.Vector2(self.width/2, self.height/2)

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getColour(self):
        return self.colour
    
    def getPos(self):
        return self.pos
    
    def getCentre(self):
        return self.centre
    
#>--------------------------------------------------------------<#

pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
clock = pg.time.Clock()
running = True
dt = 0

playerPos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

car1 = Car(40, 80, "red", (playerPos))


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    drawPos = car1.getPos() - car1.centre
    car = pg.draw.rect(screen, car1.getColour(), (*drawPos, car1.getWidth(), car1.getHeight()))

    # borderX = (car1.getCentre(), screen.get_width() - car1.getCentre())
    # borderY = (car1.getCentre(), screen.get_height() - car1.getCentre())

    # drawPos.x = max(car1.getCentre(),
    #                min(drawPos.x, screen.get_width() - car1.getCentre()))

    # drawPos.y = max(car1.getCentre(),
    #                min(drawPos.y, screen.get_height() - car1.getCentre()))



    pg.display.flip()
    clock.tick(60)
