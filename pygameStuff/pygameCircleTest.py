import pygame as pg

class Circle():
    def __init__(self, colour, radius, centre):
        self.colour = colour
        self.radius = radius
        self.centre = centre

    def getColour(self):
        return self.colour
    
    def getRadius(self):
        return self.radius
    
    def getCentre(self):
        return self.centre
    
#>--------------------------------------------------------------<#

circle1 = Circle("red", 40, (200, 200))

pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
clock = pg.time.Clock()
running = True
dt = 0

player_Pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    pg.draw.circle(screen, circle1.getColour(), player_Pos, circle1.getRadius())

    # pg.draw.circle(screen, colour, player_Pos, radius)

    borderX = (circle1.getRadius(), screen.get_width() - circle1.getRadius())
    borderY = (circle1.getRadius(), screen.get_height() - circle1.getRadius())

    player_Pos.x = max(circle1.getRadius(),
                   min(player_Pos.x, screen.get_width() - circle1.getRadius()))

    player_Pos.y = max(circle1.getRadius(),
                   min(player_Pos.y, screen.get_height() - circle1.getRadius()))



    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_Pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_Pos.y += 300 * dt
    if keys[pg.K_a]:
        player_Pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_Pos.x += 300 * dt
 
    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()