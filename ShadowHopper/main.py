import pygame as pg
import math
from classes import Character, Light

width = 1280
height = 700
def main():   #subroutine that is the main game loop 
    pg.init()
    themenuScreen = pg.display.set_mode((width, height), pg.RESIZABLE)
    clock = pg.time.Clock()
    running = True

    player = Character("red", 20, width / 2, height / 2)
    lightTest = Light(30, 60, "blue", 600, 700)
    dt = 0

    while running == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False     #functions would be called here in the main loop

        lightTest.drawLight(themenuScreen)
        
        themenuScreen.fill("black")

        player.draw(themenuScreen)
        player.movement(dt)

        pg.display.flip()

        dt = clock.tick(60) / 1000

    pg.quit()
main()


