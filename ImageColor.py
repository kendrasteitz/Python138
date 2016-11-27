# Exercise No.   1
# File Name:     ImageColor.py
# Programmer:    Kendra Steitz
# Date:          November 19, 2016
#
# Problem Statement:
#   Load an image and change it to grayscale pixel by pixel
#
# Overall Plan:
#   1. Load image
#   2. implement pseudocode that was given
#

from graphics import*

def main():

    win = GraphWin("Image", 146, 187)
    win.setBackground("White")

    img = Image(Point(73, 93.5), "fox.gif")

    column = 0
    row = 0
    img.draw(win)

    win.getMouse()

    for row in range(img.getWidth()):
        for column in range(img.getHeight()):

            r, g, b = img.getPixel(row, column)

            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))

            img.setPixel(row, column, color_rgb(brightness, brightness, brightness))
            img.save("foxGray.gif")
            win.update()

    print("Done")
    win.getMouse()
    Image(Point(73, 93.5), "foxGray.gif").draw(win)
    win.close()

main()