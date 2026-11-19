import pygame as pg

class Light(): # defines the light class that the player will have to avoid
    def __init__(self, radiusBase, radiusLight, colourBase, xLight, yLight):
        self.radiusbase = radiusBase
        self.radiuslight = radiusLight
        self.colourbase = colourBase
        self.colourlight = "white"
        self.xlight = xLight
        self.ylight = yLight
        # self.rotation = rotation
        print("helloworld")

    def getRadiusBase(self):
        return self.radiusbase

    def getRadiuslight(self):
        return self.radiuslight
    
    def getColourbase(self):
        return self.colourbase

    def getColourlight(self):
        return self.colourlight

    def getXlight(self):
        return self.xlight

    def getYLight(self):
        return self.ylight

    # def getRotation(self):
    # return self.rotation

    def drawLight(self, themenuScreen):
        pg.draw.circle(themenuScreen, self.colourlight, (self.xlight, self.ylight), self.radiuslight, draw_bottom_left=True) 
        pg.draw.circle(themenuScreen, self.colourbase, (self.xlight, self.ylight), self.radiusbase)
        