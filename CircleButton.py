# Exercise No.   3
# File Name:     CircleButton.py
# Programmer:    Kendra Steitz
# Date:          November 5, 2016
#
# Problem Statement:
#   Do everything the same as project one, but change the buttons used
#   from rectangles to circle.  Use the CButton class created.
#
# Overall Plan:
#   1. Create a window and set coordinates for it
#       GraphWin("Child Height", 400, 300)
#   2. Output the text for mother's and father's height
#   3. Create a box behind each to allow user to enter
#       each parent height
#   4. Create loop to make sure user has entered a value
#       for both of the parent's height
#           while(motherHeight <= 0 or fatherHeight <= 0):
#   5. Create if statement for if the user clicks on female or male
#   6. Have a function that takes in the gender, mother height,
#       and fathers height.  Calculate the child's estimated
#       height as an adult and return that value.
#   7. Output onto GUI the value returned from function
#       Text(Point(10, 3), "Estimated Adult Height: %.1f inches" %height).draw(win)
#

from graphics import *
from graphics import GraphWin, Point
from cbutton import CButton


def childsHeight(gender, momHeight, dadHeight):

    if gender == "male":
        heightInches = ((momHeight * 13/12) + dadHeight)/2
    if gender == "female":
        heightInches = ((dadHeight * 12/13) + momHeight)/2

    return heightInches

def main():

    win = GraphWin("Child Height", 400, 300)
    win.setCoords(0, 0, 20, 20)
    win.setBackground("white")

    Text(Point(5, 18), "Mother's Height: ").draw(win)
    Text(Point(13, 18), "inches").draw(win)
    inputMother = Entry(Point(10, 18), 6)
    inputMother.setText("0")
    inputMother.draw(win)

    Text(Point(5, 16), "Father's Height: ").draw(win)
    Text(Point(13, 16), "inches").draw(win)
    inputFather = Entry(Point(10, 16), 6)
    inputFather.setText("0")
    inputFather.draw(win)

    maleButton = CButton(win, Point(6, 12), 2, "Male")
    femaleButton = CButton(win, Point(6, 7), 2, "Female")
    maleButton.activate()
    femaleButton.activate()

    calculate = CButton(win, Point(13, 10), 3, "Calculate")

    pt = win.getMouse()

    motherHeight = eval(inputMother.getText())
    fatherHeight = eval(inputFather.getText())

    while(motherHeight <= 0 or fatherHeight <= 0):
        Text(Point(10, 3), "Please enter a height for each parent.").draw(win)
        pt = win.getMouse()
        motherHeight = eval(inputMother.getText())
        fatherHeight = eval(inputFather.getText())


    while not calculate.clicked(pt):
        if maleButton.clicked(pt):
            win.setBackground("lightBlue3")
            calculate.activate()
            pt = win.getMouse()

            if calculate.clicked(pt):
                height = childsHeight("male", motherHeight, fatherHeight)

        elif femaleButton.clicked(pt):
            win.setBackground("pink")
            calculate.activate()
            pt = win.getMouse()

            if calculate.clicked(pt):
                height = childsHeight("female", motherHeight, fatherHeight)

    Text(Point(10, 1), "Estimated Adult Height: %.1f inches" %height).draw(win)

    pt = win.getMouse()
    win.close()

main()
