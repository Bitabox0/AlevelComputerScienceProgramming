import pygame as pg

# create a program to retrieve a membership.
# take in range of detail and repeat them back.
# ask for conformation
# store these detail if confirmed
# clears if not confirmed
# allow entry of more than one membership
# store in file
# allow searching stored users - test

#>----------------------------------------------------------------<#

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Membership Storage")

baseFont = pg.font.Font(None, 32)
userText = ""

inpRectangle = pg.Rect(320, 200, 140, 32)

colourActive = pg.Color("darkgreen")

colourPassive = pg.Color("aquamarine4")
color = colourPassive

screen.fill((25, 25, 25))

textSurface = baseFont.render(userText, True, (255, 255, 255))

screen.blit(textSurface, (inpRectangle.x+5, inpRectangle.y+5))

pg.draw.rect(screen, color, inpRectangle)
pg.display.flip()

active = False

running = True
while running:
    pg.draw.rect(screen, color, inpRectangle)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if inpRectangle.collidepoint(event.pos) and not active:
                active = True
            elif inpRectangle.collidepoint(event.pos) and active:
                active = False
    if active:
        color = colourActive
    else:
        color = colourPassive
    clock.tick(60)
#>----------------------------------------------------------------<#
