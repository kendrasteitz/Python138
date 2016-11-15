# Exercise No.   2
# File Name:     roller.py
# Programmer:    Kendra Steitz
# Date:          November 5, 2016
#
# Problem Statement:
#   Create GUI with two dice and a circular button that when clicked
#   rolls the dice (uses random to output dice results).
#
# Overall Plan:
#   1. Create dice that use the DieView class.
#       Used roller class given and modified for circular buttons
#   2. Used CButton class created for rollButton and quitButton
#   3. Instead of giving a width and length, enter the radius
#
#

from random import randrange
from graphics import GraphWin, Point

from DieView import DieView
from cbutton import CButton

def main():

    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 20, 20)
    win.setBackground("green")

    die1 = DieView(win, Point(5, 15), 5)
    die2 = DieView(win, Point(15, 15), 5)

    rollButton = CButton(win, Point(6, 6), 4, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(16, 4), 2, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):

        if rollButton.clicked(pt):

            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()

        pt = win.getMouse()

    win.close()

main()

