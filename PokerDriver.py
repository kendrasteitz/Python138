# Exercise No.   1
# File Name:     DicePoker.py
# Programmer:    Kendra Steitz
# Date:          November 19, 2016
#
# Problem Statement:
#   
#
# Overall Plan:
#   1.
#
#


from PokerApp import PokerApp
from GraphicsInterface import GraphicsInterface
from Button import Button
from graphics import*

win = GraphWin("Dice Poker", 500, 600)
win.setCoords(0, 0, 50, 50)
win.setBackground("green3")

def rules():
    banner = Text(Point(25, 47), "Dice Poker Rules")
    banner.setSize(24)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)
    Text(Point(25, 43), "* Player starts with $100 and each round costs $10 to play.").draw(win)
    Text(Point(25, 40), "* The player initially rolls a completely random hand.").draw(win)
    Text(Point(25, 36), "* Player gets two chances to enhance the hand by re-rolling\nsome or all of the dice.").draw(win)
    Text(Point(25, 32), "* At the end of the hand, the player's money is updated\naccording to payout schedule.").draw(win)


def highScoresIn():
    hs = Text(Point(25, 28), "High Scores")
    hs.setSize(16)
    hs.setFill("black")
    hs.setStyle("bold")
    hs.draw(win)

    i = 26
    highScores = {}
    infile = open("C:/Users/kcste/Desktop/Python/hw12SteitzKendra/high_scores.txt", "r")
    for line in infile:
        name, score = line.split()
        Text(Point(25, i), name + "     " + score).draw(win)
        highScores[name] = score
        i = i - 2

    return highScores
    infile.close()


def highScoresOut(highScores):
    outfile = open("C:/Users/kcste/Desktop/Python/hw12SteitzKendra/high_scores.txt", "w")
    for names in highScores:
        print(names, highScores.get(names, 0), file=outfile)

    outfile.close()

def enterName():
    win = GraphWin("New High Score", 400, 200)
    win.setCoords(0, 0, 16, 20)
    win.setBackground("red")
    winner = Text(Point(8, 16), "Congratulations!")
    winner.setSize(18)
    winner.setFill("black")
    winner.setStyle("bold")
    winner.draw(win)
    Text(Point(8, 13), "You achieved a new high score!").draw(win)

    Text(Point(5, 8), "Enter Name:").draw(win)
    playerName = Entry(Point(10, 8), 15)
    playerName.setText(" ")
    playerName.draw(win)

    submit = Button(win, Point(8, 3), 6, 3, "Submit")
    submit.activate()

    pt = win.getMouse()

    winnersName = (playerName.getText())
    win.close()

    return winnersName

def main():

    rules()
    highScores = highScoresIn()

    play = Button(win, Point(13, 3), 18, 3.5, "Let's Play!")
    play.activate()
    quit = Button(win, Point(37, 3), 18, 3.5, "Quit")
    quit.activate()

    pt = win.getMouse()

    if play.clicked(pt):
        win.close()
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
        total = app.getTotalScore()

        for name in highScores:
            score = highScores.get(name, 'unknown')
            if total > int(score):
                del highScores[name]
                newName = enterName()
                highScores[newName] = total
                total = 0

    highScoresOut(highScores)
    win.close()

main()
