import pygame as pg

class Character(): # defines attributes of the character class
    def __init__(self, colour, radius, x, y):
        self.colour = colour
        self.radius = radius
        self.x = x
        self.y = y
        self.speed = 250

    def getColour(self):
        return self.colour

    def getRadius(self):
        return self.radius

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def draw(self, themenuScreen): # draws the character onto the screen
        pg.draw.circle(themenuScreen, self.colour, (self.x, self.y), self.radius)

    def movement(self, dt): # defines all the base movement keys
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y += self.speed * dt
        if keys[pg.K_a]:
            self.x -= self.speed * dt
        if keys[pg.K_s]:
            self.y -= self.speed * dt
        if keys[pg.K_d]:
            self.x += self.speed * dt

    