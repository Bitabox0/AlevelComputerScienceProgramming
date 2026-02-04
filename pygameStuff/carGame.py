import pygame as pg
import math
import random

#>--------------------------------------------------------------<#

class Car():
    def __init__(self, width, height, colour, pos):
        self.width = width
        self.height = height
        self.colour = colour
        self.pos = pos

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getColour(self):
        return self.colour
    
    def getPos(self):
        return self.pos
    
#>--------------------------------------------------------------<#

car1 = Car(20, 40, "red", (200, 200))

pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
clock = pg.time.Clock()
running = True
dt = 0

playerPos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    pg.draw.rect(screen, car1.getWidth(), playerPos, car1.getHeight())