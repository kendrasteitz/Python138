# Exercise No.   1
# File Name:     SpellCheck.py
# Programmer:    Kendra Steitz
# Date:          December 12, 2016
#
# Problem Statement:
#   Program takes in two files, one for words to know, the other to check
#   for spelling errors.
#
# Overall Plan:
#   1. Create GUI that allows input for file reading from and file with the stored
#       dictionary words.
#   2. Read in both files storing words in list.
#   3. Compare lists, outputting any words that are not found in dictionary list
#       as words misspelled.
#

from Button import Button
from graphics import*


def main():
    win = GraphWin("Spell Checker", 500, 300)
    win.setBackground("lightYellow")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Spell Check")
    banner.setSize(24)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    Text(Point(11, 11), "Enter File to Check: ").draw(win)
    textFile = Entry(Point(20, 11), 15)
    textFile.setText("")
    textFile.draw(win)

    Text(Point(11, 8), "Enter Dictionary File:").draw(win)
    dictionaryFile = Entry(Point(20, 8), 15)
    dictionaryFile.setText("")
    dictionaryFile.draw(win)

    submit = Button(win, Point(15, 3), 12, 2, "Enter")
    submit.activate()

    pt = win.getMouse()

    infileText = (textFile.getText())
    infileDictionary = (dictionaryFile.getText())

    if submit.clicked(pt):

        infile = open(infileDictionary, "r")
        textDictionary = []
        for line in infile:
            for word in line.split():
                textDictionary.append(word)
        infile.close()

        infile = open(infileText, "r")
        words = []
        for line in infile:
            for word in line.split():
                words.append(word)
        infile.close()

    print("Words misspelled:")
    for word in words:
        if word not in textDictionary:
            print(word)

    pt = win.getMouse()

    win.close()

main()
