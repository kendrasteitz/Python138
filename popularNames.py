# Exercise No.   2
# File Name:     popularNames.py
# Programmer:    Kendra Steitz
# Date:          December 12, 2016
#
# Problem Statement:
#   Allows user to input a name and outputs the rank and popularity of
#   that name
#
# Overall Plan:
#   1. Read in the text files for girls names and boys names inserting that
#       information into a dictionary (the key being the names)
#   2. Ask user to input a name
#   3. Search each dictionary for that name, if it exists output the rank
#       and popularity of it, if it does not exist output to user that name
#       is not ranked amount the top 1000 names
#

from Button import Button
from graphics import*
from string import punctuation


def main():
    infile = open("boyNames.txt", "r")
    boyNames = {}
    girlNames = {}

    i = 1
    for line in infile:
        boyName, rank = line.split()
        boyNames[boyName] = (i, rank)
        i = i + 1
    infile.close()

    infile = open("girlNames.txt", "r")
    i = 1
    for line in infile:
        girlName, rank = line.split()
        girlNames[girlName] = (i, rank)
        i = i + 1
    infile.close()

    win = GraphWin("Popularity of Names", 500, 300)
    win.setBackground("lightGreen")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Popularity of Names")
    banner.setSize(24)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    Text(Point(11, 11), "Enter Name: ").draw(win)
    name = Entry(Point(19, 11), 15)
    name.setText("")
    name.draw(win)

    submit = Button(win, Point(15, 5), 12, 2, "Check Name")
    submit.activate()

    pt = win.getMouse()

    nameInput = (name.getText())

    if submit.clicked(pt):
        if nameInput in girlNames:
            value = (girlNames.get(str(nameInput), 'default'))
            rank, popularity = str(value).split(",")
            rank = rank.replace("(", "")
            popularity = ''.join(c for c in popularity if c not in punctuation)
            print(nameInput + " is ranked " + rank + " in popularity among girls with" + popularity + " namings.")
        else:
            print(nameInput, "is not ranked among the top 1000 girl names.")

        if nameInput in boyNames:
            value = (boyNames.get(str(nameInput), 'default'))
            rank, popularity = str(value).split(",")
            rank = rank.replace("(", "")
            popularity = ''.join(c for c in popularity if c not in punctuation)
            print(nameInput + " is ranked " + rank + " in popularity among boys with" + popularity + " namings.")
        else:
            print(nameInput, "is not ranked among the top 1000 boy names.")


    win.getMouse()
    win.close()

main()
