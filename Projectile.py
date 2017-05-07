from math import sin, cos, radians


class Projectile:
    def __init__(self, angle, vel, height):
        theta = radians(angle)
        self.xpos = 0
        self.ypos = height
        self.xvel = vel * cos(theta)
        self.yvel = vel * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + self.xvel * time
        yvell = self.yvel - 9.8 * time
        self.yvel = self.yvel - 9.8 * time
        self.ypos = self.yvel * time + (self.yvel + yvell) * time/2
        self.yvel = yvell

    def getx(self):
        return self.xpos

    def gety(self):
        return self.ypos


from Projectile import *



