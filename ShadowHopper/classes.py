import pygame as pg

class Character(): # defines attributes of the character class
    def __init__(self, colour, radius, x, y):
        self.colour = colour
        self.radius = radius
        self.x = x
        self.y = y
        self.speed = 250

    def getColour(self): # returns the colour of the character
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
        if keys[pg.K_s]:
            self.y += self.speed * dt
        if keys[pg.K_a]:
            self.x -= self.speed * dt
        if keys[pg.K_w]:
            self.y -= self.speed * dt
        if keys[pg.K_d]:
            self.x += self.speed * dt

# class Light(): # defines the light class that the player will have to avoid
#     def __init__(self, radiusBase, radiusLight, colourBase, xLight, yLight):
#         self.radiusbase = radiusBase
#         self.radiuslight = radiusLight
#         self.colourbase = colourBase
#         self.colourlight = "white"
#         self.xlight = xLight
#         self.ylight = yLight
#         # self.rotation = rotation

#     def getRadiusBase(self):
#         return self.radiusbase

#     def getRadiuslight(self):
#         return self.radiuslight
    
#     def getColourbase(self):
#         return self.colourbase

#     def getColourlight(self):
#         return self.colourlight

#     def getXlight(self):
#         return self.xlight

#     def getYLight(self):
#         return self.ylight

#     # def getRotation(self):
#     # return self.rotation

#     def drawLight(self, themenuScreen):
#         pg.draw.circle(themenuScreen, self.colourbase, (self.xlight, self.ylight), self.radiusbase)
#         pg.draw.circle(themenuScreen, self.colourlight, (self.xlight, self.ylight), self.radiuslight, draw_bottom_left=True) 
