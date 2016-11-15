# Exercise No.   2
# File Name:     cbutton.py
# Programmer:    Kendra Steitz
# Date:          November 5, 2016
#
# Problem Statement:
#   Create a CBottun class that create circular buttons
#   rather than rectangle ones.
#
# Overall Plan:
#   1. Used the Button class provided as the general setup
#   2. Change the width and length to radius instead
#   3. Used self.circle = Circle(center radius) instead or Rectangle
#   4. Changed the xmax and ymax appropriately using radius
#   5. Changed roller.py to test my CButton class out
#

from graphics import *

class CButton:

    def __init__(self, win, center, radius, label):

        r = radius
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + r, x - r
        self.ymax, self.ymin = y + r, y - r
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):

        return(self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):

        return self.label.getText()

    def activate(self):

        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):

        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
